from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
import random

def gameplay():
    cenario1 = "components/background/bg1_cidade.jpg"
    cenario2 = "components/background/bg2_colinas.jpg"
    cenario3 = "components/background/bg3_floresta.jpg"
    cenarios = [cenario1, cenario2, cenario3]
    cenario = cenarios[random.randint(0, 2)]
    fundo = GameImage(cenario)
    fundo2 = GameImage(str(cenario).strip(".jpg")+"_Inverso.jpg")
    fundo2.x = janela.width

    rNuvem = 7
    nuvems = []


    objetos = []
    vidas = []
    inimigos = []
    tiros = []
    inimigosAbatidos = []

# Sprites
    ## Personagem
    passaro = Sprite("components/sprites/plane/Fly_1.png")
    passaro.x = 400
    passaro.y = janela.height / 2 - passaro.height / 2
    ## Vidas
    for i in range(0, 3):
        vid = Sprite("components/sprites/vida/vida.png")
        vid.x = vid.width * i
        vidas.append(vid)

# Variáveis
    vObstaculo = 500
    vPassaro = 400
    rload = 15
    click = 0
    reloadDano = 0
    tiroReload = 15
    rSpawnInimigo = 0
    pontos = 0

# Gameloop
    while len(vidas) > 0:

        rNuvem += 3 * janela.delta_time()

        fundo.x -= 200 * janela.delta_time()
        fundo2.x -= 200 * janela.delta_time()
        if fundo.x <= 0 - fundo.width:
            fundo.x = janela.width
        if fundo2.x <= 0 - fundo2.width:
            fundo2.x = janela.width

        fundo.draw()
        fundo2.draw()
        reloadDano -= 5 * janela.delta_time()
        rload += 9 * janela.delta_time()
        rSpawnInimigo += 9 * janela.delta_time()



        # Entradas
        if teclado.key_pressed("w") and passaro.y > 0:
            passaro.y -= vPassaro * janela.delta_time()
        if teclado.key_pressed("s") and passaro.y < 720:
            passaro.y += vPassaro * janela.delta_time()
        if teclado.key_pressed("d") and passaro.x < janela.width / 2:
            passaro.x += vPassaro * janela.delta_time()
        if teclado.key_pressed("a") and passaro.x > 0:
            passaro.x -= vPassaro * janela.delta_time()

        # Spawna nuvens###########
        if rNuvem >= 7:
            rNuvem = 0
            nuvem = Sprite("components/background/nuvem.png")
            nuvem.x = janela.width
            nuvem.y = 100 * random.randint(0, 11)
            nuvems.append(nuvem)
        if len(nuvems) > 0:
            for nuv in nuvems:
                nuv.x -= 300 * janela.delta_time()
                if nuv.x < 0 - nuv.width:
                    nuvems.remove(nuv)
                nuv.draw()
        #########################


        ## Entrada dos tiros e sua movimentação
        tiroReload += 10 * janela.delta_time()
        if teclado.key_pressed("space") and tiroReload >= 5:
            tiro = Sprite("components/sprites/bullet/Bullet_1.png")
            tiro.y = passaro.y + passaro.height / 2 - tiro.height / 2  # tiro.y = passaro.y
            tiro.x = passaro.x + tiro.width
            tiros.append(tiro)
            tiroReload = 0
        if len(tiros) > 0:
            for t in tiros:
                t.x += 500 * janela.delta_time()  # Velocidade dos tiros do personagem principal
                t.draw()
                if t.x >= 1280:
                    tiros.remove(t)

        # Projéteis Inimigos
        ## Cria
        if rload > 10:
            # posx = random.randint(1,50) # Pode ser retirado com o uso do random no obj.y
            # obj = Sprite("./coisas/imagens/bola.png")
            obj = Sprite("components/sprites/bullet/Bullet_1.png")
            obj.x = janela.width + 50
            obj.y = random.randint(0,  janela.height - obj.height)  # obj.height * posx # ??? obj.height: se diminuir o obj fica limitado a uma certa altura ??? posx: e não posy
            objetos.append(obj)
            rload = 0
        ## Verifica colisão e remove
        else:
            for o in objetos:
                if passaro.collided(o) and reloadDano < 0 and len(vidas) != 0:
                    vidas.remove(vidas[len(vidas) - 1])
                    objetos.remove(o)
                    reloadDano = 5
                o.x -= vObstaculo * janela.delta_time()
                o.draw()
                if o.x <= - o.width:
                    objetos.remove(o)

        # Inimigos
        ## Spawn Inimigos
        if rSpawnInimigo > 14 and len(inimigos) < 3:
            inimigo = Sprite("components/sprites/inimigo/inimigo1.png")
            inimigo.x = janela.width
            inimigo.y = random.randint(1, 5) * inimigo.height + 20
            inimigos.append(inimigo)
            rSpawnInimigo = 0

        ## Movimento Inimigos e Verificação de colisão com os tiros
        if len(inimigos) > 0:
            for ini in inimigos:
                if ini.x > 1100:
                    ini.x -= 100 * janela.delta_time()
                for tiro in tiros:  # Se o tiro atingir um inimigo, elimina o inimigo e remove o projétil
                    if ini.collided(tiro):
                        auxX = ini.x
                        auxY = ini.y
                        inimigos.remove(ini)
                        DIni = Sprite("components/sprites/inimigo/Dead_inimigo_1.png")
                        DIni.x = auxX
                        DIni.y = auxY
                        inimigosAbatidos.append(DIni)
                        if tiro in tiros: #isso evitar problemas se o tiro colidir 2 vezes ao mesmo tempo
                            tiros.remove(tiro)
                        pontos += 1
                ini.draw()

        if len(inimigosAbatidos) > 0:
            for deadIni in inimigosAbatidos:
                if deadIni.x >= 1000:
                    deadIni.x -= 100 * janela.delta_time()
                if deadIni.y < janela.height + deadIni.height:
                    deadIni.y += 500 * janela.delta_time()
                else:
                    inimigosAbatidos.remove(deadIni)
                deadIni.draw()

        passaro.draw()
        for vida in vidas:
            vida.draw()

        janela.draw_text(str(pontos), 20, 20, size=40, bold=True)

        if len(vidas) == 0:
            janela.clear()

        janela.update()
    gameOver = Sprite("components/sprites/game_over.png")
    gameOver.x = janela.width/2 - gameOver.width/2
    gameOver.y = janela.height/2 - gameOver.height/2
    while True:
        playerX = passaro.x
        playery = passaro.y
        passaro = Sprite("components/sprites/plane/Dead_1.png")
        passaro.x = playerX
        passaro.y = playery

        fundo.draw()
        fundo2.draw()
        passaro.draw()
        for nuv in nuvems:
            nuv.draw()
        for ini in inimigos:
            ini.draw()
        for tiro in tiros:
            tiro.draw()
        for obj in objetos:
            obj.draw()
        gameOver.draw()
        janela.draw_text(str(pontos), 20, 20, size=40, bold=True)
        janela.update()
        if teclado.key_pressed("esc"):
            return 0

def menu():
    aviao = Sprite("components/sprites/plane/Fly_1.png")
    aviao.x = janela.width/2 - aviao.width/2
    aviao.y = janela.height/2 - aviao.height/2
    fundo = GameImage("components/background/bg2_colinas.jpg")
    fundo2 = GameImage("components/background/bg2_colinas_Inverso.jpg")
    txt = Sprite("components/background/Texto.png")
    txt.x = janela.width/2 - txt.width/2
    txt.y = janela.height/4 - txt.height/2
    fundo2.x = janela.width
    vMenu = 70
    rNuvem = 7
    nuvems = []
    while True:
        fundo.x -= 50 * janela.delta_time()
        fundo2.x -= 50 * janela.delta_time()
        if fundo.x <= 0 - fundo.width:
            fundo.x = janela.width
        if fundo2.x <= 0 - fundo2.width:
            fundo2.x = janela.width

        if aviao.y >= janela.height/2 + 70:
            vMenu = - abs(vMenu)
        if aviao.y <= janela.height/2 - 70:
            vMenu = + abs(vMenu)
        aviao.y += vMenu * janela.delta_time()

        fundo.draw()
        fundo2.draw()
        aviao.draw()
        rNuvem += 2 * janela.delta_time()
        if rNuvem >= 7:
            rNuvem = 0
            nuvem = Sprite("components/background/nuvem.png")
            nuvem.x = janela.width
            nuvem.y = 100 * random.randint(0, 11)
            nuvems.append(nuvem)
        if len(nuvems) > 0:
            for nuv in nuvems:
                nuv.x -= 200 * janela.delta_time()
                if nuv.x < 0 - nuv.width:
                    nuvems.remove(nuv)
                nuv.draw()
        txt.draw()
        janela.update()
        if teclado.key_pressed("enter"):
            return 1

# Inicio

tela = 0

# Janela
janela = Window(1280, 720)
janela.set_title("PF")
teclado = Keyboard()

while True:
    if tela == 0:
        tela = menu()
    elif tela == 1:
        tela = gameplay()

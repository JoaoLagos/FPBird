from this import d
from PPlay import sprite
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
import random

def menu_principal():
    #Sprites
    ## Avião
    aviao = Sprite("components/sprites/plane/Fly_1.png")
    aviao.x = janela.width/2 - aviao.width/2
    aviao.y = janela.height/2 - aviao.height/2

    ## Fundo e Fundo2
    fundo = GameImage("components/background/bg2_colinas.jpg")
    fundo2 = GameImage("components/background/bg2_colinas_Inverso.jpg")
    fundo2.x = janela.width

    ## Logo
    logo = Sprite("components/menu/logo1.png")
    logo.x = janela.width/2 - logo.width/2
    logo.y = 100

    ## Botões
    ### Botão Jogar
    botao_jogar = Sprite("components/menu/botao_jogar.png")
    botao_jogar.x= janela.width/2 - botao_jogar.width/2
    botao_jogar.y = 300
    ### Botão Dificuldade (Nível)
    botao_dificuldade = Sprite("components/menu/botao_dificuldade.png")
    botao_dificuldade.x = janela.width/2 - botao_dificuldade.width/2
    botao_dificuldade.y = botao_jogar.y + botao_jogar.height + 20
    ### Botão Sair
    botao_sair = Sprite("components/menu/botao_sair.png")
    botao_sair.x = janela.width/2 - botao_sair.width/2
    botao_sair.y = botao_dificuldade.y + botao_dificuldade.height + 20
    
    rNuvem = 7
    nuvems = []
    while True:
        # Movimentação Fundo
        fundo.x -= 50 * janela.delta_time()
        fundo2.x -= 50 * janela.delta_time()
        if fundo.x <= 0 - fundo.width:
            fundo.x = janela.width
        if fundo2.x <= 0 - fundo2.width:
            fundo2.x = janela.width
        
        fundo.draw()
        fundo2.draw()
        logo.draw()
        
        # Criação de Nuvens
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
        
        botao_jogar.draw()
        botao_dificuldade.draw()
        botao_sair.draw()
        
        janela.update()
        if mouse_cursor.is_over_object(botao_jogar) and mouse_cursor.is_button_pressed(1):
            return 1

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
    vely_inimigos = []
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
    vely_ini = -100
    pontos = 0

# Gameloop
    ## Enquanto houver vida. len(vidas) > 0
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
            inimigo.y = random.randint(0, janela.height-inimigo.height)

            inimigos.append(inimigo)
            rSpawnInimigo = 0

        ## Movimento Inimigos e Verificação de colisão com os tiros
        if len(inimigos) > 0:
            for ini in inimigos:
                tag = inimigos.index(ini) # Foi necessário buscar a posição na lista para associar a sua vely (individualmente). Depois talvez possa melhorar
                vely_inimigos.append(vely_ini)
                
                ### Movimento dos inimigos eixo X (entrada na tela)
                if ini.x > 1100:
                    ini.x -= 100 * janela.delta_time()

                ### Movimento dos inimigos no eixo Y
                if inimigos[tag].y <= 0:
                    vely_inimigos[tag] = abs(vely_inimigos[tag])
                elif ini.y >= janela.height - ini.height:
                    vely_inimigos[tag] = -vely_inimigos[tag]

                inimigos[tag].y += vely_inimigos[tag]*janela.delta_time()

                for tiro in tiros:  # Se o tiro atingir um inimigo, elimina o inimigo e remove o projétil
                    if ini.collided(tiro):
                        auxX = ini.x
                        auxY = ini.y
                        inimigos.remove(ini)
                        DIni = Sprite("components/sprites/inimigo/Dead_inimigo_2.png") # Para criar um sprite DEAD no lugar do inimigo abatido
                        DIni.x = auxX
                        DIni.y = auxY
                        inimigosAbatidos.append(DIni)
                        if tiro in tiros: #isso evitar problemas se o tiro colidir 2 vezes ao mesmo tempo
                            tiros.remove(tiro)
                        pontos += 1
                ini.draw()

        ## Faz a queda do inimigo abatido
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

        # Se não houver mais vidas, limpa tela
        if len(vidas) == 0:
            janela.clear()
 
        janela.update()

    ## Quando a vida zerar. len(vidas) == 0
    gameOver = Sprite("components/sprites/gameover/gameover_2.png") 
    gameOver.x = janela.width/2 - gameOver.width/2
    gameOver.y = janela.height/2 - gameOver.height/2
    playerX = passaro.x
    playery = passaro.y
    passaro = Sprite("components/sprites/plane/Dead_2.png")
    passaro.x = playerX
    passaro.y = playery
    while len(vidas)==0:
        fundo.draw()
        fundo2.draw()
        # Enquanto tiver elementos passando na tela
        while len(nuvems)!=0 or len(inimigos)!=0 or len(tiros)!=0 or len(objetos)!=0:

            ## Queda do avião
            passaro.y += 400*janela.delta_time()

            ## Rolagem do Fundo
            fundo.x -= 200 * janela.delta_time()
            fundo2.x -= 200 * janela.delta_time()
            if fundo.x <= 0 - fundo.width:
                fundo.x = janela.width
            if fundo2.x <= 0 - fundo2.width:
                fundo2.x = janela.width

            fundo.draw()
            fundo2.draw()
            passaro.draw()

            ## Rolagem dos Elementos
            for nuv in nuvems:
                nuv.x -= 600 * janela.delta_time() #300
                if nuv.x < 0 - nuv.width:
                    nuvems.remove(nuv)
                nuv.draw()
            for ini in inimigos:
                ini.x -= 300 * janela.delta_time() 
                if ini.x < 0 - ini.width:
                    inimigos.remove(ini)
                ini.draw()
            for tiro in tiros:
                tiro.x -= 800*janela.delta_time() #200
                if tiro.x < 0 - tiro.width:
                    tiros.remove(tiro)
                tiro.draw()
            for obj in objetos:
                obj.x += 500*janela.delta_time() #200
                if obj.x > janela.width + obj.width:
                    objetos.remove(obj)
                obj.draw()
            
            gameOver.draw()
            janela.draw_text(str(pontos), 20, 20, size=40, bold=True)
            janela.update()

        gameOver.draw()
        janela.draw_text(f"PONTUAÇÃO: {pontos}", gameOver.x+140, gameOver.y-40, size=40, bold=True,color=(245,220,0))
        janela.draw_text("Pressione ESC para Recomeçar",gameOver.x,gameOver.y+gameOver.height,size=40,bold=True,color=(245,220,0))
        janela.update()
        if teclado.key_pressed("esc"):
            return 0

def menu_jogo():
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
menu = 0
tela = 0

# Janela
janela = Window(1280, 720)
janela.set_title("PF")
teclado = Keyboard()
mouse_cursor = Window.get_mouse()

while True:
    
    if menu == 0:
        menu = menu_principal()

    elif menu == 1:
        if tela == 0:
            tela = menu_jogo()

        elif tela == 1:
            tela = gameplay()
            menu = tela

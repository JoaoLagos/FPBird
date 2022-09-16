from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *
import random

janela = Window(1280,720)
janela.set_title("PF")
teclado = Keyboard()
objetos = []
vidas = []
inimigos = []
tiros = []
passaro = Sprite("./coisas/imagens/Fly_1.png")
fundo = Sprite("./coisas/imagens/cidade.jpg")
passaro.x = 400
passaro.y = janela.height/2 - passaro.height/2
vObstaculo = 300
vPassaro = 400
rload = 15
click = 0
reloadDano = 0
tiroReload = 15
rSpawnInimigo = 0

for i in range(0,3):
    vid = Sprite("./coisas/imagens/vida.png")
    vid.x = vid.width * i
    vidas.append(vid)

while True:
    janela.set_background_color((0,0,0))
    fundo.draw()
    reloadDano -= 5 * janela.delta_time()
    rload += 9 * janela.delta_time()
    rSpawnInimigo += 9 * janela.delta_time()

    if teclado.key_pressed("w") and passaro.y > 0:
        passaro.y -= vPassaro * janela.delta_time()
    if teclado.key_pressed("s") and passaro.y < 720:
        passaro.y += vPassaro * janela.delta_time()
    if teclado.key_pressed("d") and passaro.x + passaro.width < janela.width/2:
       passaro.x += vPassaro * janela.delta_time()
    if teclado.key_pressed("a") and passaro.x > 0:
        passaro.x -= vPassaro * janela.delta_time()

    tiroReload += 10 * janela.delta_time()
    if teclado.key_pressed("space") and tiroReload >= 5:
        tiro = Sprite("./coisas/imagens/Bullet_1.png")
        tiro.y = passaro.y + passaro.height/2 - tiro.height/2
        tiro.x = passaro.x + tiro.width
        tiros.append(tiro)
        tiroReload = 0
    if len(tiros) > 0:
        for t in tiros:
            t.x += 500 * janela.delta_time()
            t.draw()
            if t.x >= 1280:
                tiros.remove(t)

    if rload > 10:
        posx = random.randint(1,10)
        obj = Sprite("./coisas/imagens/bola.png")
        obj.x = janela.width
        obj.y = obj.height * posx
        objetos.append(obj)
        rload = 0

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

    if rSpawnInimigo > 14 and len(inimigos) < 3:
        inimigo = Sprite("./coisas/imagens/inimigo1.png")
        inimigo.x = janela.width
        inimigo.y = random.randint(1,5) * inimigo.height + 20
        inimigos.append(inimigo)
        rSpawnInimigo = 0
    if len(inimigos) > 0:
        for ini in inimigos:
            if ini.x > 1100:
                ini.x -= 100 * janela.delta_time()
            ini.draw()

    passaro.draw()
    for vida in vidas:
        vida.draw()
    janela.update()

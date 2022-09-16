from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *

janela = Window(1280,720)
janela.set_title("PF")
teclado = Keyboard()
objetos = []
vidas = []
passaro = Sprite("./coisas/imagens/bird.png")
fundo = Sprite("./coisas/imagens/floresta.jpg")
passaro.x = 400
passaro.y = janela.height/2 - passaro.height/2
v = 300
vp = 0
pv = 500
rload = 15
click = 0
reloadDano = 0
for i in range(0,3):
    vid = Sprite("./coisas/imagens/vida.png")
    vid.x = vid.width * i
    vidas.append(vid)

while True:
    janela.set_background_color((0,0,0))
    fundo.draw()
    reloadDano -= 5 * janela.delta_time()
    rload += 9 * janela.delta_time()
    if teclado.key_pressed("space") and click == 0:
        vp = -200
    if vp < 200:
        vp += 300 * janela.delta_time()
    #passaro.y += vp * janela.delta_time()
    if teclado.key_pressed("w") and passaro.y > 0:
        passaro.y -= pv * janela.delta_time()
    if teclado.key_pressed("s") and passaro.y < 720:
        passaro.y +=pv * janela.delta_time()
    if teclado.key_pressed("d") and passaro.x + passaro.width < 1280:
       passaro.x += pv * janela.delta_time()
    if teclado.key_pressed("a") and passaro.x > 0:
        passaro.x -= pv * janela.delta_time()
    if rload > 15:
        obj = Sprite("./coisas/imagens/pad2.png")
        obj.x = janela.width
        objetos.append(obj)
        obj2 = Sprite("./coisas/imagens/pad2.png")
        obj2.y = janela.height - obj.height
        obj2.x = janela.width
        objetos.append(obj2)
        rload = 0
    else:
        for o in objetos:
            if passaro.collided(o) and reloadDano < 0:
                vidas.remove(vidas[len(vidas) - 1])
                reloadDano = 5
            o.x -= v * janela.delta_time()
            o.draw()
            if o.x <= - o.width:
                objetos.remove(o)
    passaro.draw()
    for vida in vidas:
        vida.draw()
    janela.update()
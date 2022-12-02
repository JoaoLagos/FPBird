import pygame
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
import ranking
import random

''' ### FUNÇÃO COM UTILIDADE NO GAMEPLAY ### '''
''' Faz o efeito piscante no Sprite '''
def efeito_piscante(sprite, cowdownInv):
    if 5<=cowdownInv<=10 or 15<=cowdownInv<=20 or 25<=cowdownInv<=30 or 35<=cowdownInv<=40: # Gambiarra
        sprite.hide()
    else: 
        sprite.unhide()

''' Sorteia o Cenário '''
def sort_scenery():
    cenario1 = "components/background/bg1_cidade.jpg"
    cenario2 = "components/background/bg2_colinas.jpg"
    cenario3 = "components/background/bg3_floresta.jpg"
    cenario4 = "components/background/bg4_rural.jpg"
    cenario5 = "components/background/bg5_eolica.jpg"
    cenario6 = "components/background/bg6_interior.jpg"
    cenario7 = "components/background/bg7_municipio.jpg"
    cenario8 = "components/background/bg8_rio.jpg"
    cenario9 = "components/background/bg9_colinas_neve.jpg"
    cenario10 = "components/background/bg10_totem.jpg"
    cenario11 = "components/background/bg11_praia.jpg"
    cenario12 = "components/background/bg12_praia_2.jpg"
    cenarios = [cenario1, cenario2, cenario3, cenario4, cenario5, cenario6, cenario7, cenario8, cenario9, cenario10,
                cenario11, cenario12]

    scenerySorted = cenarios[random.randint(0, len(cenarios) - 1)]
    return scenerySorted

''' Lista dos Boosts '''
def lista_boost():
    global bArmor
    global bGold
    global bSpeed
    global bVida



    bArmor = ["components/sprites/boost/armor.png" , 1]
    bGold = ["components/sprites/boost/gold.png", 4]
    bSpeed = ["components/sprites/boost/speed.png", 1]
    bVida = ["components/sprites/boost/vida.png", 1]

    lista = [bArmor, bGold, bSpeed, bVida]
    return lista

''' Faz o movimento do Cenário, fundo, background '''
def rolamento_fundo(fundo, fundo2):
    fundo.x -= 200 * janela.delta_time()
    fundo2.x -= 200 * janela.delta_time()
    if fundo.x <= 0 - fundo.width:
        fundo.x = janela.width
    if fundo2.x <= 0 - fundo2.width:
        fundo2.x = janela.width
''''''''''''''''''''''''''''''''''''''''''''''''

''' ### FUNÇÕES QUE PODEM SER (FUTURAMENTE) REPRESENTADAS POR MÓDULOS ### '''
''' Menu Principal '''
def menu_principal():
    global rMouse

    # Música Menu Principal
    pygame.mixer.music.load("components/audio/menu_principal.mp3")
    pygame.mixer.music.play()

    # Sprites
    # Avião
    aviao = Sprite("components/sprites/plane/FlyAnimation.png", 2)
    aviao.set_total_duration(10)
    aviao.x = janela.width / 2 - aviao.width / 2
    aviao.y = janela.height / 2 - aviao.height / 2

    # Fundo e Fundo2
    fundo = GameImage("components/background/bg2_colinas.jpg")
    fundo2 = GameImage("components/background/bg2_colinas_Inverso.jpg")
    fundo2.x = janela.width

    # Logo
    logo = Sprite("components/menu/logo1.png")
    logo.x = janela.width / 2 - logo.width / 2
    logo.y = 100

    # Botões
    # Botão Jogar
    botao_jogar = Sprite("components/menu/botao_jogar.png")
    botao_jogar.x = janela.width / 2 - botao_jogar.width / 2
    xJogar = botao_jogar.x
    botao_jogar.y = 300
    yJogar = botao_jogar.y
    # Botão Dificuldade (Nível)
    botao_dificuldade = Sprite("components/menu/botao_dificuldade.png")
    botao_dificuldade.x = janela.width / 2 - botao_dificuldade.width / 2
    xDificuldade = botao_dificuldade.x
    botao_dificuldade.y = botao_jogar.y + botao_jogar.height + 20
    yDificuldade = botao_dificuldade.y
    # Botão Sair
    botao_sair = Sprite("components/menu/botao_sair.png")
    botao_sair.x = janela.width / 2 - botao_sair.width / 2
    botao_sair.y = botao_dificuldade.y + botao_dificuldade.height + 20
    # "Botão" Ranking
    botao_ranking = Sprite("components/menu/botao_ranking_Fechado.png")
    botao_ranking.x = janela.width - botao_ranking.width - 30
    xRanking = botao_ranking.x
    botao_ranking.y = (botao_jogar.y + botao_jogar.height) - botao_ranking.height/2 
    yRanking = botao_ranking.y
    ## Logo Ranking
    logo_ranking = Sprite("components/menu/ranking2.png")
    logo_ranking.x = botao_ranking.x + 20
    logo_ranking.y = botao_ranking.y - 110
    ## Seta Ranking
    seta_ranking = Sprite("components/menu/seta_ranking.png")
    seta_ranking.x = botao_ranking.x + botao_ranking.width/2 - 5
    seta_ranking.y = botao_ranking.y- seta_ranking.height - 20
    ySetaRanking = seta_ranking.y

    rNuvem = 7
    nuvems = []
    velSetaRanking = 10
    while True:
        # Movimentação
        ## Movimentação Fundo
        fundo.x -= 50 * janela.delta_time()
        fundo2.x -= 50 * janela.delta_time()
        if fundo.x <= 0 - fundo.width:
            fundo.x = janela.width
        if fundo2.x <= 0 - fundo2.width:
            fundo2.x = janela.width
        ##Movimentação Seta Ranking
        seta_ranking.y += velSetaRanking*janela.delta_time()
        logo_ranking.y += velSetaRanking*janela.delta_time()
        if seta_ranking.y <= ySetaRanking:
            velSetaRanking = abs(velSetaRanking)
        if seta_ranking.y >= botao_ranking.y-seta_ranking.height:
            velSetaRanking = -(velSetaRanking)

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
        botao_ranking.draw()
        logo_ranking.draw()
        seta_ranking.draw()

        janela.update()

        if rMouse > 0: # Recarregamento do clique, pois senão ele pode dar double click.
            rMouse -= 10 * janela.delta_time()
        # Seleção das opções
        #BOTÂO JOGAR
        if mouse_cursor.is_over_object(botao_jogar):
            botao_jogar = Sprite("components/menu/botao_jogar_UP.png")
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                rMouse = 5
                pygame.mixer.music.unload()
                return 1
        else:
            botao_jogar = Sprite("components/menu/botao_jogar.png")
        botao_jogar.x = xJogar
        botao_jogar.y = yJogar
        # BOTÃO DIFICULDADE
        if mouse_cursor.is_over_object(botao_dificuldade):
            botao_dificuldade = Sprite("components/menu/botao_dificuldade_UP.png")
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                rMouse = 5
                return 2
        else:
            botao_dificuldade = Sprite("components/menu/botao_dificuldade.png")
        botao_dificuldade.x = xDificuldade
        botao_dificuldade.y = yDificuldade

        # BOTÃO SAIR
        if mouse_cursor.is_over_object(botao_sair) and mouse_cursor.is_button_pressed(1) and rMouse <= 0:
            janela.close()
        # BOTÃO RANKING
        if mouse_cursor.is_over_object(botao_ranking):
            botao_ranking = Sprite("components/menu/botao_ranking_UP.png")
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
               ranking.start() 
        else:
            botao_ranking = Sprite("components/menu/botao_ranking_fechado.png")
        botao_ranking.x = xRanking
        botao_ranking.y = yRanking
''' Gameplay '''
def gameplay():
    # Cenários
    ''' Sorteia o cenário e cria o fundo (1 e 2, o reverso) '''
    cenario = sort_scenery() # Sorteia Cenário
    fundo = GameImage(cenario)
    fundo2 = GameImage(str(cenario).strip(".jpg") + "_Inverso.jpg")
    fundo2.x = janela.width
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    rNuvem = 7
    nuvems = []

    objetos = []
    vidas = []
    inimigos = []
    vely_inimigos = []
    tiros = []
    inimigosAbatidos = []
    listaFogo = []

    boosts = lista_boost()
    boostsAtivos = []
    rBoostSpeed_ON = 0

    # Sprites
    # Personagem
    passaro = Sprite("components/sprites/plane/FlyAnimation.png", 2)
    passaro.set_total_duration(10)
    
    passaro.x = 400
    passaro.y = janela.height / 2 - passaro.height / 2
    # Vidas
    for i in range(0, 3):
        vid = Sprite("components/sprites/vida/vida.png")
        vid.x = vid.width * i
        vid.y = 5
        vidas.append(vid)

    # Variáveis
    vObstaculo = 350 + 150 * nivel
    vPassaro = 400
    rBulletInimigo = 15
    click = 0
    tiroReload = 15
    rSpawnInimigo = 0
    vely_ini = -100 - 20*nivel
    velx_tirosAliados = 500
    qtd_inimigosAbatidos = 0
    reloadInvencivel = 0
    invencivel_ByDano = False
    invencivel_ByBoost = False
    if nivel == 1: #Fácil
        rBulletInimigo_TIME = 10
        rSpawnInimigo_TIME = 14
    elif nivel == 2: #Médio
        rBulletInimigo_TIME = 7
        rSpawnInimigo_TIME = 10
    elif nivel == 3: #Difícil
        rBulletInimigo_TIME = 4
        rSpawnInimigo_TIME = 4

    # FPS
    tempo = 0
    FPS = 0
    frames = 0

    # Gameloop
    # Enquanto houver vida. len(vidas) > 0
    while len(vidas) > 0:
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

        tempo += janela.delta_time()
        frames += 1
        if tempo >= 1:
            FPS = frames
            frames = 0
            tempo = 0
        rNuvem += 3 * janela.delta_time()

        rolamento_fundo(fundo, fundo2) # Faz o fundo andar
        fundo.draw()
        fundo2.draw()

        rBulletInimigo += 9 * janela.delta_time()
        rSpawnInimigo += 9 * janela.delta_time()

        # Entradas
        if teclado.key_pressed("w") and passaro.y > 0:
            passaro.y -= vPassaro * janela.delta_time()
        if teclado.key_pressed("s") and passaro.y + passaro.height < 720:
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

        # Entrada dos tiros e sua movimentação
        tiroReload += 10 * janela.delta_time()
        if teclado.key_pressed("space") and tiroReload >= 5:
            somTiro = pygame.mixer.Sound("components/audio/tiro.wav")
            somTiro.play()
            tiro = Sprite("components/sprites/bullet/Bullet_1.png")
            tiro.y = passaro.y + passaro.height / 2 - tiro.height / 2  # tiro.y = passaro.y
            tiro.x = passaro.x + tiro.width
            tiros.append(tiro)
            tiroReload = 0
        if len(tiros) > 0:
            for t in tiros:
                t.x += velx_tirosAliados * janela.delta_time()  # Velocidade dos tiros do personagem principal
                t.draw()
                if t.x >= 1280:
                    tiros.remove(t)

        # Projéteis Inimigos
        # Cria
        if rBulletInimigo > rBulletInimigo_TIME:
            # posx = random.randint(1,50) # Pode ser retirado com o uso do random no obj.y
            # obj = Sprite("./coisas/imagens/bola.png")
            obj = Sprite("components/sprites/bullet/Bullet_1.png")
            obj.x = janela.width + 50
            obj.y = random.randint(0, janela.height - obj.height)  # obj.height * posx # ??? obj.height: se diminuir o obj fica limitado a uma certa altura ??? posx: e não posy
            objetos.append(obj)
            rBulletInimigo = 0
        # Verifica colisão e remove
        else:
            for o in objetos:
                o.x -= vObstaculo * janela.delta_time()
                if reloadInvencivel <=0: # Para validar a colisão, caso não tenha sido atingido recentemente
                    # Colisão com a nave
                    if passaro.collided(o) and len(vidas) != 0:
                        somCrash1 = pygame.mixer.Sound(
                            "components/audio/crash.wav")
                        somCrash1.play()
                        vidas.remove(vidas[len(vidas) - 1])
                        objetos.remove(o)

                        #Sprite Fogos
                        fogo = Sprite("components/sprites/plane/fire.png", 7)
                        fogo.set_total_duration(500)
                        #fogo.set_sequence(0, 7, loop=False) # Para tirar o loop da animação. Nem precisa, pq a gente remove o Sprite mais abaixo
                        fogo.x = passaro.x
                        fogo.y = passaro.y
                        listaFogo.append(fogo)

                        reloadInvencivel = 40 # Deixar invensível por um tempo, contagem mais abaixo
                        invencivel_ByDano = True
                #Colisão com a parede
                if o.x <= - o.width:
                    objetos.remove(o)
                o.draw()
        
        # Carregamento da Invencibilidade
        if reloadInvencivel > 0:

            if invencivel_ByDano:
                reloadInvencivel -= 25*janela.delta_time()
                efeito_piscante(passaro, reloadInvencivel) # Efeito Piscante 
                if reloadInvencivel <= 0:
                    invencivel_ByDano = False

            elif invencivel_ByBoost:
                reloadInvencivel -= 25*janela.delta_time()
                if reloadInvencivel <= 0:
                    xAux = passaro.x
                    yAux = passaro.y
                    passaro = Sprite("components/sprites/plane/FlyAnimation.png", 2)
                    passaro.set_total_duration(10)
                    passaro.x = xAux
                    passaro.y = yAux

                    invencivel_ByBoost = False

        # Inimigos
        # Spawn Inimigos
        if rSpawnInimigo > rSpawnInimigo_TIME and len(inimigos) < 2 + nivel:
            inimigo = Sprite("components/sprites/inimigo/inimigoAnimation.png", 2)
            inimigo.set_total_duration(10)
            inimigo.x = janela.width
            inimigo.y = random.randint(0, janela.height - inimigo.height)

            inimigos.append(inimigo)
            rSpawnInimigo = 0

        # Movimento Inimigos e Verificação de colisão com os tiros
        if len(inimigos) > 0:
            for ini in inimigos:
                tag = inimigos.index(
                    ini)  # Foi necessário buscar a posição na lista para associar a sua vely (individualmente). Depois talvez possa melhorar
                vely_inimigos.append(vely_ini)

                # Movimento dos inimigos eixo X (entrada na tela)
                if ini.x > 1100:
                    ini.x -= 100 * janela.delta_time()

                # Movimento dos inimigos no eixo Y
                if inimigos[tag].y <= 0:
                    vely_inimigos[tag] = abs(vely_inimigos[tag])
                elif ini.y >= janela.height - ini.height:
                    vely_inimigos[tag] = -vely_inimigos[tag]

                inimigos[tag].y += vely_inimigos[tag] * janela.delta_time()

                for tiro in tiros:  # Se o tiro atingir um inimigo, elimina o inimigo e remove o projétil
                    if ini.collided(tiro):
                        # Som Crash
                        somCrash2 = pygame.mixer.Sound(
                            "components/audio/crash.wav")
                        somCrash2.play()

                        #Sprite Fogos
                        fogo = Sprite("components/sprites/plane/fire.png", 7)
                        fogo.set_total_duration(500)
                        #fogo.set_sequence(0, 7, loop=False) # Para tirar o loop da animação. Nem precisa, pq a gente remove o Sprite mais abaixo
                        fogo.x = ini.x
                        fogo.y = ini.y
                        listaFogo.append(fogo)

                        #Saida do Boost
                        if qtd_inimigosAbatidos%2 == 0:
                            boost = boosts[random.randint(0,len(boosts)-1)]
                            spriteBoost = Sprite(boost[0], boost[1])

                            if boost[1]>1:
                               spriteBoost.set_total_duration(250) 
                            spriteBoost.x = ini.x
                            spriteBoost.y = ini.y
                            boostsAtivos.append([spriteBoost, boost[0]])

                        auxX = ini.x
                        auxY = ini.y
                        inimigos.remove(ini)
                        DIni = Sprite(
                            "components/sprites/inimigo/Dead_inimigo_2.png")  # Para criar um sprite DEAD no lugar do inimigo abatido
                        DIni.x = auxX
                        DIni.y = auxY
                        inimigosAbatidos.append(DIni)
                        if tiro in tiros:  # isso evitar problemas se o tiro colidir 2 vezes ao mesmo tempo
                            tiros.remove(tiro)
                        qtd_inimigosAbatidos += 1
                        if qtd_inimigosAbatidos <= 20:
                            vObstaculo += 20
                ini.update()
                ini.draw()

        # Saida do Fogo
        for fogo in listaFogo:
            fogo.x -= 200 * janela.delta_time()
            fogo.y -= 50 * janela.delta_time()
            fogo.update()
            fogo.draw()
            if fogo.curr_frame==6: #Se for o ultimo frame, remove, para não ficar em loop
                listaFogo.remove(fogo)

        # Saída do Boost
        for boost in boostsAtivos:
            boost[0].x -= vObstaculo * janela.delta_time()
            ## Se sair da tela, remove
            if boost[0].x < 0 - boost[0].width:
                boostsAtivos.remove(boost)
            ## Se colidir com o player, dê o boost e remova
            if boost[0].collided(passaro):
                '''
                DAR O BOOST PARA O PLAYER:
                Se for Armor -> Dá Armor
                Se for Life -> Dá Life
                Se for Energy -> Dá Energy
                Se for Gold -> Dá Gold
                '''
                if boost[1] == bArmor[0] and reloadInvencivel<=0: # ARMOR ### Tem que colocar reloadInvencivel<=0 para as vezes não bugar, pq se colidir com o bullet inimigo e dps pegar armor, o sprite fica travado no FlyAnimation_Armor.png
                    xAux = passaro.x
                    yAux = passaro.y
                    passaro = Sprite("components/sprites/plane/FlyAnimation_Armor.png", 2)
                    passaro.set_total_duration(10)
                    passaro.x = xAux
                    passaro.y = yAux

                    reloadInvencivel = 40
                    invencivel_ByBoost = True
                if boost[1] == bGold[0]: # GOLD
                    print("B") #### DO
                    '''
                    Dar Gold
                    '''
                if boost[1] == bSpeed[0]:
                    rBoostSpeed_ON = 1000 * janela.delta_time()
                if boost[1] == bVida[0]:
                    if len(vidas)<3:
                        vid = Sprite("components/sprites/vida/vida.png")
                        vid.x = vid.width * (len(vidas))
                        vid.y = 5
                        vidas.append(vid)

                boostsAtivos.remove(boost)
            
        
            if boost[0].total_frames > 1: # Fazer isso, pois se o total_frames for 1 (default), o .update da erro.
                boost[0].update() # Importante para dar o efeito de animação há mais de um frame.
            boost[0].draw()

        # Boost -> Validação (daqueles que ficam por um tempo, no caso da vida, é só adicionar +1, então não entra pois não há temporizador)
        # SPEED
        if rBoostSpeed_ON>0:
            vPassaro = 1000
            rBoostSpeed_ON -= 1*janela.delta_time()
        else: 
            vPassaro = 400
        

        # Faz a queda do inimigo abatido
        if len(inimigosAbatidos) > 0:
            for deadIni in inimigosAbatidos:
                if deadIni.x >= 1000:
                    deadIni.x += 100 * janela.delta_time()
                if deadIni.y < janela.height + deadIni.height:
                    deadIni.y += 500 * janela.delta_time()
                else:
                    inimigosAbatidos.remove(deadIni)
                deadIni.draw()

        passaro.draw()
        passaro.update()
        for vida in vidas:
            vida.draw()

        janela.draw_text(f"Inimigos Abatidos:{qtd_inimigosAbatidos}", 3, 25, size=25, bold=True)

        if pygame.key.get_pressed()[pygame.K_F5]:
            janela.draw_text("FPS: {}".format(FPS), janela.width -
                             100, 0, size=16, bold=True, color=(0, 235, 12))
        if teclado.key_pressed("esc"):
            return 0

        # Se não houver mais vidas, limpa tela
        if len(vidas) == 0:
            janela.clear()

        janela.update()

    # Quando a vida zerar. len(vidas) == 0
    gameOver = Sprite("components/sprites/gameover/gameover_2.png")
    gameOver.x = janela.width / 2 - gameOver.width / 2
    gameOver.y = janela.height / 2 - gameOver.height / 2
    playerX = passaro.x
    playery = passaro.y
    passaro = Sprite("components/sprites/plane/Dead_2.png")
    passaro.x = playerX
    passaro.y = playery
    while len(vidas) == 0:
        fundo.draw()
        fundo2.draw()
        pygame.mixer.music.load("components/audio/gameover.wav")
        pygame.mixer.music.play()
        if not pygame.mixer.music.get_busy:
            pygame.mixer.music.unload()
        # Enquanto tiver elementos passando na tela
        while len(nuvems) != 0 or len(inimigos) != 0 or len(tiros) != 0 or len(objetos) != 0:

            # Queda do avião
            passaro.y += 400 * janela.delta_time()

            # Rolagem do Fundo
            fundo.x -= 200 * janela.delta_time()
            fundo2.x -= 200 * janela.delta_time()
            if fundo.x <= 0 - fundo.width:
                fundo.x = janela.width
            if fundo2.x <= 0 - fundo2.width:
                fundo2.x = janela.width

            fundo.draw()
            fundo2.draw()
            passaro.draw()

            # Rolagem dos Elementos
            for nuv in nuvems:
                nuv.x -= 600 * janela.delta_time()  # 300
                if nuv.x < 0 - nuv.width:
                    nuvems.remove(nuv)
                nuv.draw()
            for ini in inimigos:
                ini.x -= 300 * janela.delta_time()
                if ini.x < 0 - ini.width:
                    inimigos.remove(ini)
                ini.draw()
            for tiro in tiros:
                tiro.x -= 800 * janela.delta_time()  # 200
                if tiro.x < 0 - tiro.width:
                    tiros.remove(tiro)
                tiro.draw()
            for obj in objetos:
                obj.x += 500 * janela.delta_time()  # 200
                if obj.x > janela.width + obj.width:
                    objetos.remove(obj)
                obj.draw()

            gameOver.draw()
            janela.update()

        gameOver.draw()
        janela.draw_text("PONTUAÇÃO: {}".format(qtd_inimigosAbatidos), gameOver.x +
                         140, gameOver.y - 40, size=40, bold=True, color=(245, 220, 0))
        janela.draw_text("Pressione ESC para Recomeçar", gameOver.x, gameOver.y +
                         gameOver.height, size=40, bold=True, color=(245, 220, 0))
        janela.update()
        if teclado.key_pressed("esc"):
            return 0

''' Menu do Jogo '''
def menu_jogo():
    aviao = Sprite("components/sprites/plane/FlyAnimation.png", 2)
    aviao.set_total_duration(10)
    aviao.x = janela.width / 2 - aviao.width / 2
    aviao.y = janela.height / 2 - aviao.height / 2

    fundo = GameImage("components/background/bg2_colinas.jpg")
    fundo2 = GameImage("components/background/bg2_colinas_Inverso.jpg")
    fundo2.x = janela.width

    txt = Sprite("components/background/Texto.png")
    txt.x = janela.width / 2 - txt.width / 2
    txt.y = janela.height / 4 - txt.height / 2

    vMenu = 70
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

        # Movimentação Avião
        if aviao.y >= janela.height / 2 + 70:
            vMenu = - abs(vMenu)
        if aviao.y <= janela.height / 2 - 70:
            vMenu = + abs(vMenu)
        aviao.y += vMenu * janela.delta_time()

        fundo.draw()
        fundo2.draw()
        aviao.draw()
        aviao.update()

        # Criação das nuvens
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

''' Dificuldade '''
def dificuldade():
    global nivel  # Pega por referência a variável nível para ser modificada dentro e fora da função
    global rMouse
    fundo = GameImage("components/background/bg2_colinas.jpg")

    # Botões
    # Texto Dificuldade
    txt_dificuldade = Sprite("components/menu/dificuldade/dificuldade.png", 1)
    txt_dificuldade.x = janela.width / 2 - txt_dificuldade.width / 2
    txt_dificuldade.y = 20

    # Fácil
    facil = Sprite("components/menu/dificuldade/facil.png", 1)
    facil.x = janela.width / 2 - facil.width / 2
    facil.y = 200

    # Médio
    medio = Sprite("components/menu/dificuldade/medio.png", 1)
    medio.x = janela.width / 2 - medio.width / 2
    medio.y = facil.y + facil.height + 20

    # Dificil
    dificil = Sprite("components/menu/dificuldade/dificil.png", 1)
    dificil.x = janela.width / 2 - dificil.width / 2
    dificil.y = medio.y + medio.height + 20

    # Voltar
    voltar = Sprite("components/menu/dificuldade/voltar2.png", 1)
    voltar.x = 40
    voltar.y = janela.height - voltar.height - 20

    while True:
        if rMouse > 0:
            rMouse -= 10 * janela.delta_time()

        if mouse_cursor.is_over_object(facil) and mouse_cursor.is_button_pressed(1) and rMouse <= 0:
            nivel = 1
            rMouse = 5
            return 0
        if mouse_cursor.is_over_object(medio) and mouse_cursor.is_button_pressed(1) and rMouse <= 0:
            nivel = 2
            rMouse = 5
            return 0
        if mouse_cursor.is_over_object(dificil) and mouse_cursor.is_button_pressed(1) and rMouse <= 0:
            nivel = 3
            rMouse = 5
            return 0
        if mouse_cursor.is_over_object(voltar) and mouse_cursor.is_button_pressed(1) and rMouse <= 0:
            return 0

        fundo.draw()
        txt_dificuldade.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        voltar.draw()
        janela.update()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Inicio
menu = 0
tela = 0
nivel = 1
rMouse = 0

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

    elif menu == 2:
        menu = dificuldade()

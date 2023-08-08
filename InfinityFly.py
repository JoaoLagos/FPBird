import pygame
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
import ranking
import random


def draw_text(surface, text, pos, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

''' Função para obter o tamanho do texto sem renderizá-lo na tela '''
def get_text_size(text, size):
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, BLACK)
    return text_surface.get_width(), text_surface.get_height()

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
    global bShoot
    global bSpeed
    global bLife



    bArmor = ["components/sprites/boost/armor.png" , 1]
    bShoot = ["components/sprites/boost/specialShoot.png", 4]
    bSpeed = ["components/sprites/boost/speed.png", 1]
    bLife = ["components/sprites/boost/life.png", 4]

    lista = [bArmor, bShoot, bSpeed, bLife]
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
    xSair = botao_sair.x
    botao_sair.y = botao_dificuldade.y + botao_dificuldade.height + 20
    ySair = botao_sair.y
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
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

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
        if mouse_cursor.is_over_object(botao_sair):
            botao_sair = Sprite("components/menu/botao_sair_UP.png")
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                janela.close()
        else:
            botao_sair = Sprite("components/menu/botao_sair.png")
        botao_sair.x = xSair
        botao_sair.y = ySair

        # BOTÃO RANKING
        if mouse_cursor.is_over_object(botao_ranking):
            botao_ranking = Sprite("components/menu/botao_ranking_UP.png")
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                rMouse = 5
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
    rBoostShoot_ON = 0
    # Sprites
    # Personagem
    passaro = Sprite("components/sprites/plane/FlyAnimation.png", 2)
    passaro.set_total_duration(140)
    
    passaro.x = 400
    passaro.y = janela.height / 2 - passaro.height / 2
    # Vidas
    for i in range(0, 3):
        vid = Sprite("components/sprites/vida/vida.png")
        vid.x = vid.width * i + 3*i +16
        vid.y = 20
        vidas.append(vid)
    # Caixa Transparente
    transparentBox = Sprite("components/sprites/caixa_transparente2.png")

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
    BOSS_is_ON = False
    collision_in_Janela_Width = False
    pontos = 0
    decaimentoPontos = 0 #Fator de divisão que aumenta com o passar do tempo, e reseta ao atingir um inimigo
    if nivel == 1: #Fácil
        rBulletInimigo_TIME = 7
        rSpawnInimigo_TIME = 14
        vBoost = 600
        resetBoost = 4
    elif nivel == 2: #Médio
        rBulletInimigo_TIME = 6
        rSpawnInimigo_TIME = 10
        vBoost = 700
        resetBoost = 5
    elif nivel == 3: #Difícil
        rBulletInimigo_TIME = 4
        rSpawnInimigo_TIME = 4
        vBoost = 800
        resetBoost = 6

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
            # Bullet Normal ou Bullet Boost
            somTiro = pygame.mixer.Sound("components/audio/tiro.wav")
            somTiro.play()
            if rBoostShoot_ON<=0:
                tiro = Sprite("components/sprites/bullet/bullet.png")
            else:
                tiro = Sprite("components/sprites/bullet/Bullet_BOOST_Animation2.png", 4)
            tiro.set_total_duration(20)

            tiro.y = passaro.y + passaro.height / 2 - tiro.height / 2  # tiro.y = passaro.y
            tiro.x = passaro.x + tiro.width
            tiros.append(tiro)
            tiroReload = 0
        if len(tiros) > 0:
            for t in tiros:
                t.x += velx_tirosAliados * janela.delta_time()  # Velocidade dos tiros do personagem principal
                t.update()
                t.draw()
                if t.x >= 1280:
                    tiros.remove(t)

        # Projéteis Inimigos
        # Cria
        if rBulletInimigo > rBulletInimigo_TIME:
            # posx = random.randint(1,50) # Pode ser retirado com o uso do random no obj.y
            # obj = Sprite("./coisas/imagens/bola.png")
            obj = Sprite("components/sprites/bullet/bulletInimigoAnimation.png", 2)
            obj.set_total_duration(20)
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
                o.update()
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
            if BOSS_is_ON == False:
                inimigo = Sprite("components/sprites/inimigo/bossAnimation2.png", 2)
                vidaBOSS = 3
                BOSS_is_ON = True
                isBOSS = True
            else:
                inimigo = Sprite("components/sprites/inimigo/InimigoAnimation.png", 2)
                isBOSS = False
            inimigo.set_total_duration(10)
            inimigo.x = janela.width
            inimigo.y = random.randint(0, janela.height - inimigo.height)

            inimigos.append([inimigo, isBOSS])
            rSpawnInimigo = 0

        # Movimento Inimigos e Verificação de colisão com os tiros
        if len(inimigos) > 0:
            for ini in inimigos:
                tag = inimigos.index(
                    ini)  # Foi necessário buscar a posição na lista para associar a sua vely (individualmente). Depois talvez possa melhorar
                vely_inimigos.append(vely_ini)

                # Movimento dos inimigos eixo X (entrada na tela)
                if ini[0].x > 1100:
                    ini[0].x -= 100 * janela.delta_time()

                # Movimento dos inimigos no eixo Y
                if inimigos[tag][0].y <= 0:
                    vely_inimigos[tag] = abs(vely_inimigos[tag])
                elif inimigos[tag][0].y >= janela.height - ini[0].height:
                    vely_inimigos[tag] = -vely_inimigos[tag]

                inimigos[tag][0].y += vely_inimigos[tag] * janela.delta_time()

                for tiro in tiros:  # Se o tiro atingir um inimigo, elimina o inimigo e remove o projétil
                    if ini[0].collided(tiro):
                        if ini[1]==True and vidaBOSS>1: # Se o inimigo for isBOSS = True
                            vidaBOSS-=1
                        else:
                            if ini[1]==True: # Se o inimigo for isBOSS = True
                                BOSS_is_ON = False
                                DIni = Sprite(
                                "components/sprites/inimigo/Dead_boss.png")  # Para criar um sprite DEAD no lugar do inimigo abatido
                            else:
                                DIni = Sprite(
                                "components/sprites/inimigo/Dead_inimigo_2.png")  # Para criar um sprite DEAD no lugar do inimigo abatido
                            auxX = ini[0].x
                            auxY = ini[0].y
                            inimigos.remove(ini)
                            DIni.x = auxX
                            DIni.y = auxY
                            inimigosAbatidos.append(DIni)
                            qtd_inimigosAbatidos += 1
                            
                            #Saida do Boost
                            if qtd_inimigosAbatidos%resetBoost == 0:
                                boost = boosts[random.randint(0,len(boosts)-1)]
                                spriteBoost = Sprite(boost[0], boost[1])
                                if boost[1]>1:
                                    spriteBoost.set_total_duration(250) 
                                spriteBoost.x = ini[0].x
                                spriteBoost.y = ini[0].y
                                boostsAtivos.append([spriteBoost, boost[0]])

                        # Som Crash
                        somCrash2 = pygame.mixer.Sound(
                            "components/audio/crash.wav")
                        somCrash2.play()

                        #Sprite Fogos
                        fogo = Sprite("components/sprites/plane/fire.png", 7)
                        fogo.set_total_duration(500)
                        #fogo.set_sequence(0, 7, loop=False) # Para tirar o loop da animação. Nem precisa, pq a gente remove o Sprite mais abaixo
                        fogo.x = ini[0].x
                        fogo.y = ini[0].y
                        listaFogo.append(fogo)

                        if tiro in tiros:  # isso evitar problemas se o tiro colidir 2 vezes ao mesmo tempo
                            tiros.remove(tiro)
                        
                        if qtd_inimigosAbatidos <= 20:
                            vObstaculo += 20

                        pontos += int((10/decaimentoPontos)//1) #Incrementa pontos
                        decaimentoPontos = 1 #Reseta o fator decaimentoPontos
                        break # Caso um inimigo seja atingido por 2 tiros, da bug. Com esse break resolve
                ini[0].update()
                ini[0].draw()

        decaimentoPontos += janela.delta_time() # Incrementa no decaimentoPontos com o passar do tempo

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
            boost[0].x -= vBoost * janela.delta_time()
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
                Se for Gold -> Dá Gold ???
                '''
                if boost[1] == bArmor[0] and reloadInvencivel<=0: # ARMOR ### Tem que colocar reloadInvencivel<=0 para as vezes não bugar, pq se colidir com o bullet inimigo e dps pegar armor, o sprite fica travado no FlyAnimation_Armor.png
                    xAux = passaro.x
                    yAux = passaro.y
                    passaro = Sprite("components/sprites/plane/FlyAnimation_Armor.png", 2)
                    passaro.set_total_duration(10)
                    passaro.x = xAux
                    passaro.y = yAux

                    reloadInvencivel = 90
                    invencivel_ByBoost = True
                if boost[1] == bShoot[0]: 
                    rBoostShoot_ON = 620 * janela.delta_time()
                if boost[1] == bSpeed[0]:
                    rBoostSpeed_ON = 1000 * janela.delta_time()
                if boost[1] == bLife[0]:
                    if len(vidas)<3:
                        vid = Sprite("components/sprites/vida/vida.png")
                        vid.x = vid.width * (len(vidas)) + 3*(len(vidas)) + 16
                        vid.y = 20
                        vidas.append(vid)

                boostsAtivos.remove(boost)
            
        
            if boost[0].total_frames > 1: # Fazer isso, pois se o total_frames for 1 (default), o .update da erro.
                boost[0].update() # Importante para dar o efeito de animação há mais de um frame.
            boost[0].draw()

        # Boost -> Validação (daqueles que ficam por um tempo, no caso da vida, é só adicionar +1, então não entra pois não há temporizador)
        # GOLD
        if rBoostShoot_ON>0:
            tiroReload += 15 * janela.delta_time()
            rBoostShoot_ON -= 1*janela.delta_time()
            if rBoostShoot_ON<=0:
               tiroReload += 10 * janela.delta_time()    
        
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
        transparentBox.draw()
        for vida in vidas:
            vida.draw()

        janela.draw_text(f"Inimigos Abatidos: {qtd_inimigosAbatidos}", 19, 70, size=19, bold=True)
        janela.draw_text(f"Pontos: {pontos:d}", 19, 100, size=19, bold=True)

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
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

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
                ini[0].x -= 300 * janela.delta_time()
                if ini[0].x < 0 - ini[0].width:
                    inimigos.remove(ini)
                ini[0].update()
                ini[0].draw()
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
        janela.draw_text("PONTUAÇÃO: {}".format(pontos), gameOver.x +
                         140, gameOver.y - 40, size=40, bold=True, color=(245, 220, 0))
        janela.draw_text("Pressione ESC para Recomeçar", gameOver.x, gameOver.y +
                         gameOver.height, size=40, bold=True, color=(245, 220, 0))
        janela.update()
        if teclado.key_pressed("esc"):
            janela.clear()
            bg = GameImage("components/background/bg2_colinas.jpg") 

            logo = Sprite("components/menu/logo1.png")
            logo.x = janela.width/2 - logo.width/2
            logo.y = 35

            nuvem = Sprite("components/sprites/nuvem.png")
            nuvem.x = (janela.width - nuvem.width) // 2
            nuvem.y = (janela.height - nuvem.height) // 2

            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            running = True
            avisoTamanho = False
            avisoEspaco = False

            color_index = 0
            colors = [(255, 255, 0), (255, 0, 0)]
            color_change_interval = 500  # Tempo em milissegundos (500ms = 0.5 segundos)
            last_color_change_time = pygame.time.get_ticks()
            # Tamanho da caixa de entrada
            input_box_width = 200
            input_box_height = 36
            # Posição centralizada horizontalmente e verticalmente para a caixa de entrada
            input_box_x = (janela.width - input_box_width) // 2
            input_box_y = (janela.height - input_box_height) // 2
            nickname_text = "Nickname:"
            nickname_width, nickname_height = get_text_size(nickname_text, 36)
            nickname_x = janela.width // 2 - nickname_width//2
            nickname_y = input_box_y - 30
            input_text = ""
            clock = pygame.time.Clock()

            while running:
                bg.draw()
                for event in pygame.event.get(): #pygame.key.get_pressed()[pygame.K_F11]
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_RETURN]:
                            nickname = input_text
                            print("Nickname inserido:", nickname)
                            if not len(nickname)==0:
                                running = False
                            else:
                                avisoTamanho = True
                                avisoEspaco = False

                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            new_char = event.unicode
                            if new_char != " ":
                                new_text = input_text + new_char
                                text_width, text_height = get_text_size(new_text, 28)
                                if text_width <= input_box_width - 20:
                                    input_text = new_text
                            elif new_char == " ": #else
                                avisoEspaco = True
                                avisoTamanho = False



                # Textos
                nuvem.draw()
                input_box = pygame.Rect(input_box_x+10, input_box_y+30-20, input_box_width, input_box_height)
                pygame.draw.rect(janela.screen, BLACK, input_box, 4)
                draw_text(janela.screen, nickname_text, (nickname_x+10, input_box_y - 30+30-20), 36, BLACK)
                draw_text(janela.screen, input_text, (input_box_x + 10+10, input_box_y + 10+30-20), 28, BLACK)

                # Verifica se é hora de alternar a cor
                current_time = pygame.time.get_ticks()
                if current_time - last_color_change_time >= color_change_interval:
                    last_color_change_time = current_time
                    color_index = (color_index + 1) % len(colors)
                if avisoTamanho:
                    draw_text(janela.screen,"AVISO: Insira um nome.",(input_box_x,input_box_y + input_box_height + 40-20), 20, colors[color_index])
                elif avisoEspaco:
                    draw_text(janela.screen,"AVISO: Não é permitido espaço.",(input_box_x,input_box_y + input_box_height + 40-20), 20, colors[color_index])

                logo.draw()

                pygame.display.flip()
                clock.tick(60)

            ranking.savePoints(nickname, pontos)
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
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

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
    xFacil = facil.x
    facil.y = 200
    yFacil = facil.y

    # Médio
    medio = Sprite("components/menu/dificuldade/medio.png", 1)
    medio.x = janela.width / 2 - medio.width / 2
    xMedio = medio.x
    medio.y = facil.y + facil.height + 20
    yMedio = medio.y

    # Dificil
    dificil = Sprite("components/menu/dificuldade/dificil.png", 1)
    dificil.x = janela.width / 2 - dificil.width / 2
    xDificil = dificil.x
    dificil.y = medio.y + medio.height + 20
    yDificil = dificil.y
    # Voltar
    voltar = Sprite("components/menu/dificuldade/voltar2.png", 1)
    voltar.x = 40
    xVoltar = voltar.x
    voltar.y = janela.height - voltar.height - 20
    yVoltar = voltar.y
    while True:
        if pygame.key.get_pressed()[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

        if rMouse > 0:
            rMouse -= 10 * janela.delta_time()

        # FACIL
        if mouse_cursor.is_over_object(facil):
            facil = Sprite("components/menu/dificuldade/facil_UP.png", 1)
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                nivel = 1
                rMouse = 5
                return 0
        else:
            facil = Sprite("components/menu/dificuldade/facil.png", 1)
        facil.x = xFacil
        facil.y = yFacil

        # MEDIO
        if mouse_cursor.is_over_object(medio):
            medio =Sprite("components/menu/dificuldade/medio_UP.png", 1)
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                nivel = 2
                rMouse = 5
                return 0
        else:
            medio =Sprite("components/menu/dificuldade/medio.png", 1)
        medio.x = xMedio
        medio.y = yMedio

        # DIFÍCIL
        if mouse_cursor.is_over_object(dificil):
            dificil = Sprite("components/menu/dificuldade/dificil_UP.png", 1)
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                nivel = 3
                rMouse = 5
                return 0
        else:
            dificil = Sprite("components/menu/dificuldade/dificil.png", 1)
        dificil.x = xDificil
        dificil.y = yDificil

        # SAIR
        if mouse_cursor.is_over_object(voltar):
            voltar =Sprite("components/menu/dificuldade/voltar2_UP.png", 1)
            if mouse_cursor.is_button_pressed(1) and rMouse <= 0:
                return 0
        else:
            voltar =Sprite("components/menu/dificuldade/voltar2.png", 1)
        voltar.x = xVoltar
        voltar.y = yVoltar

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

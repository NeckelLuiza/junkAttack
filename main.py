import pygame 
import time
from recursos.utils import aguarde, ouvir
from recursos.utils import salvar_partida, mostrar_ultimos_logs
import tkinter as tk
import random
from tkinter import messagebox

pygame.init()

#tela
tamanho = (1000,700)
tela = pygame.display.set_mode( tamanho ) 
relogio = pygame.time.Clock()
pygame.display.set_caption("Junk Attack")
icone  = pygame.image.load("recursos/icone.png")
pygame.display.set_icon(icone)
#cenário
fundoStart= pygame.image.load("recursos/fundoStart.png")
fundoJogo = pygame.image.load("recursos/fundoJogo.png")
regras = pygame.image.load("recursos/regras.png")
placar = pygame.image.load("recursos/placar.png")
logoMercado = pygame.image.load("recursos/logoMercado.png")
logoMercadoRed = pygame.image.load("recursos/logoMercadoRed.png")
aviao = pygame.image.load("recursos/aviao.png")
coracao = pygame.image.load("recursos/coracao.png")
tecla = pygame.image.load("recursos/tecla.png")
panfleto = pygame.image.load("recursos/panfleto.png")
#personagem
personagemInicio= pygame.image.load("recursos/personagemInicio.png")
personagemMagro = pygame.image.load("recursos/personagem1.png")
magroComendo = pygame.image.load("recursos/p1Comendo.png")
magroDireita = pygame.image.load("recursos/p1Direita.png")
magroEsquerda = pygame.image.load("recursos/p1Esquerda.png")
personagemCheio = pygame.image.load("recursos/personagem2.png")
cheioComendo = pygame.image.load("recursos/p2Comendo.png")
cheioDireita = pygame.image.load("recursos/p2Direita.png")
cheioEsquerda = pygame.image.load("recursos/p2Esquerda.png")
personagemGordo = pygame.image.load("recursos/personagem3.png")
gordoComendo = pygame.image.load("recursos/p3Comendo.png")
gordoDireita = pygame.image.load("recursos/p3Direita.png")
gordoEsquerda = pygame.image.load("recursos/p3Esquerda.png")
personagemFinal = pygame.image.load("recursos/personagemFinal.png")
#comidas
banana = pygame.image.load("recursos/banana.png")
batataFrita = pygame.image.load("recursos/batataFrita.png")
chocolate = pygame.image.load("recursos/chocolate.png")
hamburguer = pygame.image.load("recursos/hamburguer.png")
laranja = pygame.image.load("recursos/laranja.png")
maca = pygame.image.load("recursos/maca.png")
melancia = pygame.image.load("recursos/melancia.png")
morango = pygame.image.load("recursos/morango.png")
ovos = pygame.image.load("recursos/ovos.png")
pizza = pygame.image.load("recursos/pizza.png")
refrigerante = pygame.image.load("recursos/refrigerante.png")
sorvete = pygame.image.load("recursos/sorvete.png")
#sons
trilhaSonora = pygame.mixer.music.load("recursos/trilhaSonora.mp3")
pygame.mixer.music.set_volume(0.7) 
audioPorta = pygame.mixer.Sound("recursos/audioPorta.mp3")
audioComer = pygame.mixer.Sound("recursos/audioComer.mp3")
audioComer.set_volume(0.5)
audioEngordar = pygame.mixer.Sound("recursos/audioEngordar.mp3")  
audioBotao = pygame.mixer.Sound("recursos/audioBotao.mp3")
audioPerder = pygame.mixer.Sound("recursos/fail.mp3")
audioPerder.set_volume(0.3)
#cores
branco = (255,255,255)
preto = (0, 0 ,0 )
bege= (71,51,34)
amarelo = (238,177,94) 
#fontes
fonteBotaoGrande = pygame.font.Font("recursos/BebasNeue.ttf", 40)
fonteBotaoM = pygame.font.Font("recursos/BebasNeue.ttf", 30)
fonteBotao= pygame.font.Font("recursos/BebasNeue.ttf", 20)
fonteGizPequeno = pygame.font.Font("recursos/giz.otf", 10)
fonteGiz = pygame.font.Font("recursos/giz.otf", 20)
fonteGizMédio = pygame.font.Font("recursos/giz.otf", 25)
fonteGizMaior = pygame.font.Font("recursos/giz.otf", 40)
pygame.mixer.music.load("recursos/trilhaSonora.mp3")

def start():
    def obter_nome():
        global nome
        nome = ""
        enviado = False

        root = tk.Tk()
        largura_janela = 350
        altura_janela = 130
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        root.title("Fale ou digite seu nome")

        label = tk.Label(root, text="Jogador:")
        label.pack()

        entry_nome = tk.Entry(root)
        entry_nome.pack(pady=5)

        def ouvir_nome():
            texto = ouvir()
            if texto:
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, texto)
                root.update()
            else:
                messagebox.showwarning("Aviso", "Não consegui entender o que você disse.")

        def enviar_nome():
            nonlocal enviado
            global nome
            nome = entry_nome.get()
            if not nome:
                messagebox.showwarning("Aviso", "Por favor, diga ou digite seu nome!")
            else:
                pygame.mixer.Sound.play(audioPorta)
                enviado = True
                root.destroy()

        botao_ouvir = tk.Button(root, text="Falar agora", command=ouvir_nome)
        botao_ouvir.pack()

        botao_enviar = tk.Button(root, text="Enviar", command=enviar_nome)
        botao_enviar.pack(pady=5)

        root.mainloop()
        return enviado  

    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    larguraButtonStart = 120
    alturaButtonStart  = 50
    larguraButtonQuit = 120
    alturaButtonQuit  = 50
    xCentro = 190 + 120 // 2  
    yCentroStart = 340 + 50 // 2
    yCentroQuit = 400 + 50 // 2
    posicaoXAviao = 1000
    posicaoYAviao = 120

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 110
                    alturaButtonStart  = 45
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 110
                    alturaButtonQuit  = 45

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonStart = 120
                    alturaButtonStart  = 50
                    tela.fill(branco)
                    tela.blit(fundoStart, (0,0))
                    tela.blit(personagemInicio, (500, 200))
                    tela.blit(logoMercado,(780, 0))
                    tela.blit(aviao, (posicaoXAviao, posicaoYAviao))

                    startButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonStart // 2, yCentroStart - alturaButtonStart // 2, larguraButtonStart, alturaButtonStart), border_radius=15)
                    startTexto = fonteBotao.render("Iniciar", True, preto)
                    rectTexto = startTexto.get_rect(center=startButton.center)
                    tela.blit(startTexto, rectTexto)

                    quitButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonQuit // 2, yCentroQuit - alturaButtonQuit // 2, larguraButtonQuit, alturaButtonQuit), border_radius=15)
                    quitTexto = fonteBotao.render("Sair", True, preto)
                    rectTextoQuit = quitTexto.get_rect(center=quitButton.center)
                    tela.blit(quitTexto, rectTextoQuit)

                    pygame.display.update()
                    pygame.time.delay(120)
                    if obter_nome():
                        instrucoes()  

                if quitButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonQuit = 120
                    alturaButtonQuit  = 50
                    tela.fill(branco)
                    tela.blit(fundoStart, (0,0))
                    tela.blit(personagemInicio, (500, 200))
                    tela.blit(logoMercado,(780, 0))
                    tela.blit(aviao, (posicaoXAviao, posicaoYAviao))

                    startButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonStart // 2, yCentroStart - alturaButtonStart // 2, larguraButtonStart, alturaButtonStart), border_radius=15)
                    startTexto = fonteBotao.render("Iniciar", True, preto)
                    rectTexto = startTexto.get_rect(center=startButton.center)
                    tela.blit(startTexto, rectTexto)

                    quitButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonQuit // 2, yCentroQuit - alturaButtonQuit // 2, larguraButtonQuit, alturaButtonQuit), border_radius=15)
                    quitTexto = fonteBotao.render("Sair", True, preto)
                    rectTextoQuit = quitTexto.get_rect(center=quitButton.center)
                    tela.blit(quitTexto, rectTextoQuit)

                    pygame.display.update()
                    pygame.time.delay(150)
                    quit()
                        
        tela.fill(branco)
        tela.blit(fundoStart, (0,0) )
        tela.blit(personagemInicio, (500, 200) )
        tela.blit(logoMercado,(780, 0))
        tela.blit(aviao, (posicaoXAviao, posicaoYAviao))
        if posicaoXAviao > -1120:
            posicaoXAviao = posicaoXAviao - 16
            posicaoYAviao = posicaoYAviao -1
        
        startButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonStart // 2,yCentroStart - alturaButtonStart // 2, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteBotao.render("Iniciar", True, preto)
        rectTexto = startTexto.get_rect(center=startButton.center)
        tela.blit(startTexto, rectTexto)
        
        quitButton = pygame.draw.rect(tela, amarelo, (xCentro - larguraButtonQuit // 2,  yCentroQuit - alturaButtonQuit // 2, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteBotao.render("Sair", True, preto)
        rectTextoQuit = quitTexto.get_rect(center=quitButton.center)
        tela.blit(quitTexto, rectTextoQuit)
        
        pygame.display.update()
        relogio.tick(60)

def instrucoes():
    larguraButtonStart = 80
    alturaButtonStart  = 50
    larguraButtonQuit = 80
    alturaButtonQuit  = 50
    xCentroStart = 305 + 80 // 2  
    xCentroQuit = 190 + 80 // 2
    yCentroStart = 605 + 50 // 2
    yCentroQuit = 605 + 50 // 2

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 70
                    alturaButtonStart  = 45
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 70
                    alturaButtonQuit  = 45

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonStart = 80
                    alturaButtonStart  = 50
                    jogo()
                if quitButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonQuit = 80
                    alturaButtonQuit  = 50
                    aguarde(0.2)
                    start()

        tela.fill(branco)
        tela.blit(fundoJogo, (0,0) )
        tela.blit(regras, (0, -10))
        centro_x = 468 + 326 // 2  # 631
        texto_boas_vindas = fonteGizMédio.render(f"Bem-vindo(a), {nome}!", True, preto)
        rect_boas_vindas = texto_boas_vindas.get_rect(center=(centro_x, 300))
        tela.blit(texto_boas_vindas, rect_boas_vindas)

        startButton = pygame.draw.rect(tela, amarelo, (xCentroStart - larguraButtonStart // 2,yCentroStart - alturaButtonStart // 2, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteBotaoGrande.render(">", True, preto)
        rectTexto = startTexto.get_rect(center=startButton.center)
        tela.blit(startTexto, rectTexto)
        
        quitButton = pygame.draw.rect(tela, amarelo, (xCentroQuit - larguraButtonQuit // 2,  yCentroQuit - alturaButtonQuit // 2, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteBotaoGrande.render("<", True, preto)
        rectTextoQuit = quitTexto.get_rect(center=quitButton.center)
        tela.blit(quitTexto, rectTextoQuit)
        
        pygame.display.update()
        relogio.tick(60)

def jogo():
    largura_original, altura_original = logoMercadoRed.get_size()
    escala = 1.0
    direcao = 1  
    velocidade = 0.001
    escala_min = 0.95
    escala_max = 1.05
    posicaoXpersonagem = 300
    posicaoYpersonagem = 400
    movimentopersonagem  = 0
    pontos = 0
    vidas = 3
    vidas_antes = 3
    invulneravel = False
    tempo_invulneravel = 0
    duracao_invulneravel = 1000
    tempo_inicio = time.time()
    tempo_total_pausa = 0
    tempo_ultimo_panfleto = pygame.time.get_ticks()
    intervalo_panfleto = random.randint(5000, 10000)

    class Panfleto:
        def __init__(self):
            self.imagem = pygame.image.load("recursos/panfleto.png")
            self.resetar()

        def resetar(self):
            self.y = random.randint(100, 500)
            direcao_esquerda = random.choice([True, False])
                    
            if direcao_esquerda:
                self.x = -self.imagem.get_width()  # esquerda
                self.vx = random.uniform(0.2, 0.5)  # velocidade para a direita
            else:
                self.x = 1000  # direita
                self.vx = -random.uniform(0.2, 0.5)  # velocidade para a esquerda

            self.ativo = True

        def mover(self):
            if self.ativo:
                self.x += self.vx
                if self.x > 1000:  # Saiu da tela
                    self.ativo = False

        def desenhar(self, superficie):
            if self.ativo:
                superficie.blit(self.imagem, (self.x, self.y))

    def sortear_comida():
        if random.random() < 0.6:  
            return random.choice(saudaveis)
        else:
            return random.choice(nao_saudaveis)

    panfleto = Panfleto()

    class Comida:
        def __init__(self, imagem):
            self.imagem = imagem
            self.x = random.randint(50, 800)
            self.y = -random.randint(50, 300)
            self.velocidade = random.uniform(0.5, 1.2)

        def atualizar(self):
            self.y += self.velocidade
            if self.y > 700:
                self.y = -random.randint(100, 300)
                self.x = random.randint(50, 800)
                self.velocidade = random.uniform(0.5, 1.2)
                self.imagem = sortear_comida()

        def desenhar(self, superficie):
            superficie.blit(self.imagem, (self.x, self.y))



    saudaveis = [banana, laranja, maca, melancia, morango]
    nao_saudaveis = [batataFrita, chocolate, hamburguer, ovos, pizza, refrigerante, sorvete]
    comidas_saudaveis = [Comida(random.choice(saudaveis)) for _ in range(3)]
    comidas_nao_saudaveis = [Comida(random.choice(nao_saudaveis)) for _ in range(3)]
    comidas = comidas_saudaveis + comidas_nao_saudaveis
    random.shuffle(comidas)

    personagem_atual = personagemMagro
    personagemFrente = personagemMagro
    personagemComendo = magroComendo
    esquerda_img = magroEsquerda
    direita_img = magroDireita

    def pausar_jogo():
        nonlocal tempo_total_pausa  

        pausado = True
        overlay = pygame.Surface((1000, 700))  
        overlay.set_alpha(180)  
        overlay.fill((0, 0, 0))  

        texto_pausa = fonteGiz.render("Jogo Pausado - Pressione ESPAÇO para continuar", True, branco)
        rect_texto = texto_pausa.get_rect(center=(500, 350))

        tempo_pausa_inicio = time.time()

        while pausado:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        pausado = False

            tela.blit(fundoJogo, (0, 0))
            tela.blit(logoMercadoRed, (0, 0))
            tela.blit(ponto, (710, 175))
            tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))
            tela.blit(personagem_atual, (posicaoXpersonagem, posicaoYpersonagem))
            if vidas == 3:
                tela.blit(coracao, (820, 0))
            if vidas >= 2:
                tela.blit(coracao, (850, 0))
            if vidas >= 1:
                tela.blit(coracao, (880, 0))
            tela.blit(overlay, (0, 0))
            tela.blit(texto_pausa, rect_texto)
            pygame.display.update()

        tempo_pausa_fim = time.time()
        tempo_total_pausa += tempo_pausa_fim - tempo_pausa_inicio  

    while True:
        tempo_atual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    movimentopersonagem = 3
                    personagem_atual = direita_img
                elif evento.key == pygame.K_LEFT:
                    movimentopersonagem = -3
                    personagem_atual = esquerda_img
                elif evento.key == pygame.K_SPACE:
                    pausar_jogo()
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                    movimentopersonagem = 0
                    personagem_atual = personagemFrente

        posicaoXpersonagem += movimentopersonagem
        posicaoXpersonagem = max(15, min(posicaoXpersonagem, 705))
        boca_x = posicaoXpersonagem + 100
        boca_y = posicaoYpersonagem + 110
        hitbox_boca = pygame.Rect(boca_x, boca_y, 60, 40)

        if invulneravel and tempo_atual - tempo_invulneravel > duracao_invulneravel:
            invulneravel = False

        for comida in comidas:
            panfleto.mover()
            comida.atualizar()

        for comida in comidas:
            comida_rect = pygame.Rect(comida.x, comida.y, comida.imagem.get_width(), comida.imagem.get_height())
            if hitbox_boca.colliderect(comida_rect) and not invulneravel:
                if comida.imagem in saudaveis:
                    pontos += 1
                    audioComer.play()
                    comida.y = -random.randint(100, 300)
                    comida.x = random.randint(50, 800)
                    comida.imagem = sortear_comida()
                    panfleto.mover()
                    personagem_atual = personagemComendo
                    tela.fill(branco)
                    tela.blit(fundoJogo, (0, 0))

                    tela.blit(logoMercadoRed, (0, 0))

                    ponto = fonteGiz.render("Pontos", True, branco)
                    tela.blit(ponto, (710, 175))
                    tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))
                    if vidas == 3:
                        tela.blit(coracao, (820, 0))
                    if vidas >= 2:
                        tela.blit(coracao, (850, 0))
                    if vidas >= 1:
                        tela.blit(coracao, (880, 0))
                    for c in comidas:
                        c.desenhar(tela)
                    panfleto.desenhar(tela)
                    tela.blit(personagem_atual, (posicaoXpersonagem, posicaoYpersonagem))
                    tela.blit(teclaTexto, (855, 65))
                    tela.blit(tecla, (910, 56))
                    panfleto.desenhar(tela)
                    pygame.display.update()
                    pygame.time.delay(100)
                    personagem_atual = personagemFrente

                else:
                    vidas_antes = vidas
                    audioComer.play()
                    audioEngordar.play()
                    invulneravel = True
                    tempo_invulneravel = tempo_atual
                    comida.y = -random.randint(100, 300)
                    comida.x = random.randint(50, 800)
                    comida.imagem = sortear_comida()
                    personagem_atual = personagemComendo

                    tela.fill(branco)
                    tela.blit(fundoJogo, (0, 0))
                    tela.blit(logoMercadoRed, (0, 0))
                    ponto = fonteGiz.render("Pontos", True, branco)
                    tela.blit(ponto, (710, 175))
                    tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))

                    if vidas == 3:
                        tela.blit(coracao, (820, 0))
                    if vidas >= 2:
                        tela.blit(coracao, (850, 0))
                    if vidas >= 1:
                        tela.blit(coracao, (880, 0))

                    for c in comidas:
                        c.desenhar(tela)

                    tela.blit(personagem_atual, (posicaoXpersonagem, posicaoYpersonagem))
                    tela.blit(teclaTexto, (855, 65))
                    tela.blit(tecla, (910, 56))
                    panfleto.desenhar(tela)
                    pygame.display.update()
                    pygame.time.delay(150)
                    personagem_atual = personagemFrente

                    vidas -= 1

                    if vidas == 0:
                        for i in range(6):
                            tela.fill(branco)
                            tela.blit(fundoJogo, (0, 0))
                            tela.blit(logoMercadoRed, (0, 0))
                            ponto = fonteGiz.render("Pontos", True, branco)
                            tela.blit(ponto, (710, 175))
                            tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))
                            if i % 2 == 0:
                                tela.blit(coracao, (880, 0))
                            tela.blit(personagemComendo, (posicaoXpersonagem, posicaoYpersonagem))
                            pygame.display.update()
                            pygame.time.delay(100)

                        tela.fill(branco)
                        tela.blit(fundoJogo, (0, 0))
                        tela.blit(logoMercadoRed, (0, 0))
                        tela.blit(fonteGiz.render("Pontos", True, branco), (710, 175))
                        tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))
                        tela.blit(personagemFinal, (posicaoXpersonagem, posicaoYpersonagem))
                        pygame.mixer.Sound.play(audioPerder)
                        pygame.display.update()
                        pygame.time.delay(3000)
        
                        tempo_final = time.time()
                        duracao = tempo_final - tempo_inicio - tempo_total_pausa
                        duracao_formatada = time.strftime("%H:%M:%S", time.gmtime(duracao))
                        salvar_partida(nome, pontos, duracao_formatada)
                        dead()
                        return

                    if vidas == 3:
                        personagemFrente = personagemMagro
                        personagemComendo = magroComendo
                        esquerda_img = magroEsquerda
                        direita_img = magroDireita
                    elif vidas == 2:
                        personagemFrente = personagemCheio
                        personagemComendo = cheioComendo
                        esquerda_img = cheioEsquerda
                        direita_img = cheioDireita
                    elif vidas == 1:
                        personagemFrente = personagemGordo
                        personagemComendo = gordoComendo
                        esquerda_img = gordoEsquerda
                        direita_img = gordoDireita

        mostrar_personagem = not (invulneravel and (tempo_atual // 100) % 2 == 1)

        tela.fill(branco)
        tela.blit(fundoJogo, (0, 0))

        escala += velocidade * direcao
        if escala >= escala_max or escala <= escala_min:
            direcao *= -1

        nova_largura = int(largura_original * escala)
        nova_altura = int(altura_original * escala)
        logo_animada = pygame.transform.scale(logoMercadoRed, (nova_largura, nova_altura))

        x_original = 0  
        y_original = 0  
        x_logo = x_original + (largura_original - nova_largura) // 2
        y_logo = y_original + (altura_original - nova_altura) // 2
        tela.blit(logo_animada, (x_logo, y_logo))

        ponto = fonteGiz.render("Pontos", True, branco)
        tela.blit(ponto, (710, 175))
        tela.blit(fonteGizMaior.render(str(pontos), True, branco), (740, 200))

        if invulneravel and (tempo_atual // 100) % 2 == 0:
            if vidas_antes == 3:
                tela.blit(coracao, (820, 0))
            if vidas_antes >= 2:
                tela.blit(coracao, (850, 0))
            if vidas_antes >= 1:
                tela.blit(coracao, (880, 0))
        else:
            if vidas == 3:
                tela.blit(coracao, (820, 0))
            if vidas >= 2:
                tela.blit(coracao, (850, 0))
            if vidas >= 1:
                tela.blit(coracao, (880, 0))

        if mostrar_personagem:
            tela.blit(personagem_atual, (posicaoXpersonagem, posicaoYpersonagem))

        for comida in comidas:
            comida.desenhar(tela)
        
        if not panfleto.ativo:
            tempo_agora = pygame.time.get_ticks()
            if tempo_agora - tempo_ultimo_panfleto >= intervalo_panfleto:
                panfleto.resetar()
                tempo_ultimo_panfleto = tempo_agora
                intervalo_panfleto = random.randint(30000, 500000)

        panfleto.mover()
        panfleto.desenhar(tela)


        teclaTexto = fonteBotao.render("Pausar", True, branco)
        tela.blit(teclaTexto, (855, 65))
        tela.blit(tecla, (910, 56))

        pygame.display.update()

def dead():
    larguraButtonStart = 150
    alturaButtonStart  = 50
    larguraButtonQuit = 150
    alturaButtonQuit  = 50
    xCentroStart = 240 + 250 // 2  
    xCentroQuit = 685 + 250 // 2
    yCentro = 600 + 50 // 2

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 45
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 45

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonStart = 150
                    alturaButtonStart  = 50
                    start()
                if quitButton.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(audioBotao)
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 50
                    aguarde(0.2)
                    quit()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0) )
        tela.blit(placar, (60,-15))
        tela.blit(personagemFinal, (-30, 300))

        mostrar_ultimos_logs(tela)

        startButton = pygame.draw.rect(tela, amarelo, (xCentroStart - larguraButtonStart // 2,yCentro - alturaButtonStart // 2, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteBotao.render("Jogar novamente", True, preto)
        rectTexto = startTexto.get_rect(center=startButton.center)
        tela.blit(startTexto, rectTexto)
        
        quitButton = pygame.draw.rect(tela, amarelo, (xCentroQuit - larguraButtonQuit // 2,  yCentro - alturaButtonQuit // 2, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteBotao.render("Sair", True, preto)
        rectTextoQuit = quitTexto.get_rect(center=quitButton.center)
        tela.blit(quitTexto, rectTextoQuit)
        
        pygame.display.update()
        relogio.tick(60)    

start()
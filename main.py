import pygame 
import os
from recursos.utils import limpar_tela, aguarde
import tkinter as tk

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
jornal = pygame.image.load("recursos/jornal.png")
logoMercado = pygame.image.load("recursos/logoMercado.png")
logoMercadoRed = pygame.image.load("recursos/logoMercadoRed.png")
aviao = pygame.image.load("recursos/aviao.png")
coracao = pygame.image.load("recursos/coracao.png")
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
trilhaSonora = pygame.mixer.Sound("recursos/trilhaSonora.mp3")
audioPorta = pygame.mixer.Sound("recursos/audioPorta.mp3")
audioComer = pygame.mixer.Sound("recursos/audioComer.mp3")
audioEngordar = pygame.mixer.Sound("recursos/audioEngordar.mp3")
#cores
branco = (255,255,255)
preto = (0, 0 ,0 )
bege= (71,51,34)
amarelo = (238,177,94) 
#fontes
fonteBotao= pygame.font.Font("recursos/BebasNeue.ttf", 20)
fonteTitulo= pygame.font.Font("recursos/BebasNeue.ttf", 60)
fonteGiz = pygame.font.Font("recursos/giz.otf", 20)
fonteGizMaior = pygame.font.Font("recursos/giz.otf", 40)
pygame.mixer.music.load("recursos/trilhaSonora.mp3")

def start():
        tela.fill(branco)
        tela.blit(fundoStart, (0,0) )
        tela.blit(personagemInicio, (500, 200) )
        tela.blit(logoMercado,(780, 0))

        #botões start/quit

        pygame.display.update()
        relogio.tick(60)

def instrucoes():
        tela.fill(branco)
        tela.blit(jornal, (0,0) )


def jogo():
        tela.fill(branco)
        tela.blit(fundoJogo, (0,0) )


def dead():
    tela.fill(branco)
    tela.blit(jornal, (0,0) )

start()
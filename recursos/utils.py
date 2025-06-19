import os
import time
import random
import pygame
import speech_recognition as controladorVoz
from datetime import datetime

def limparTela():
    os.system("cls")
    
def aguarde(segundos):
    time.sleep(segundos)

recognizer = controladorVoz.Recognizer()
def ouvir():
    with controladorVoz.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=3)
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except controladorVoz.UnknownValueError:
            print("Não consegui entender o que você disse.")
            return ""
        except controladorVoz.RequestError:
            print("Erro ao se conectar com o servidor!")
            return ""
    
def salvar_partida(nome, pontos, duracao):
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    with open("log.dat", "a") as f:
        f.write(f"{nome};{pontos};{data};{duracao}\n")

def mostrar_ultimos_logs(surface):
    fontePixel= pygame.font.Font("recursos/pixel.ttf", 20)
    corBorda=(57,45,11)
    try:
        with open("log.dat", "r") as f:
            linhas = f.readlines()[-5:]
            linhas.reverse()
    except FileNotFoundError:
        linhas = []

    largura_caixa = 190
    altura_caixa = 110
    espacamento_x = 15
    espacamento_y = 6

    base_x = 490  # mais para a direita
    base_y = 290  # mais para cima

    for i, linha in enumerate(linhas):
        try:
            nome, pontos, data, duracao = linha.strip().split(";")
        except ValueError:
            continue

        coluna = i % 2  # 0 ou 1
        linha_idx = i // 2  # 0, 1 ou 2

        x = base_x + coluna * (largura_caixa + espacamento_x)
        y = base_y + linha_idx * (altura_caixa + espacamento_y)

        surface.blit(fontePixel.render(f"{i+1}. Jogador: {nome}", True, corBorda), (x + 10, y + 10))
        surface.blit(fontePixel.render(f"Pontos: {pontos}", True, corBorda), (x + 30, y + 35))
        surface.blit(fontePixel.render(f"Duração: {duracao}", True, corBorda), (x + 30, y + 60))
        surface.blit(fontePixel.render(f"Data: {data}", True, corBorda), (x + 30, y + 80))
 
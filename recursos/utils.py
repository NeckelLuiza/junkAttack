import os
import time
import random
import pygame
import speech_recognition as controladorVoz

def limparTela():
    os.system("cls")
    
def aguarde(segundos):
    time.sleep(segundos)
    
def inicializarBancoDeDados():
    # r - read, w - write, a - append
    try:
        banco = open("registro.partidas","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("registro.partidas","w")

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
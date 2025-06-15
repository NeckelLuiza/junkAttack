import os
import time


def limpar_tela():
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
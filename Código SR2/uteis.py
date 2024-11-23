#Arquivo para colocar as funções uteis sem ser os menus
import json
import os
import re
import sys
from time import sleep
from menus import *

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    

def escrever_arquivo(arquivo, dados):
    try:
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {e}.")
    

def ler_escrever_arquivo(arquivo):

    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({}, f, indent=4)

    with open(arquivo, 'r') as f:
        return json.load(f)
    

def listar():

    print()
    print()
    print("       " + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m')
    print("       " + '\033[1mLista de Compras:\033[m')
    print()

def buscar():

    os.system('cls')
    print()
    print()
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + "  " * 10 + '\033[1;30;44mSISTEMA ENGINSTOCK:\033[m' + " " * 23 + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " + "=" * 60 + " " + "|")
    print("  " + "|" + " " + '-' * 60 + " " + "|")
    print("  " + "|" + " " * 62 + "|")
    print("  " + "|" + " " * 20 + '\033[1mBuscar Compras:\033[m' + " " * 27 + "|")
    print("  " + "|" + " " * 20 + " " * 42 + "|")


def att_compra():

    print("1 - Atualizar Nome do Produto Comprado.")
    print("2 - Atualizar Quantidade Comprada.")
    print("3 - Atualizar Tempo de Entrega.")
    print("4 - Atualizar Valor Total da Compra")
    print("5 - Atualizar CNPJ do Fornecedor.")


def validar_codigo(codigo, dicionario):

    if not re.match(r"^C\d{3}$", codigo) or not codigo in dicionario:
        print("Código Inválido!")
        sleep(3)
        sys.exit()
    else:
        print("Código Válido!")
        sleep(1.5)


def validar_cnpj(cnpj_fornecedor):

    if not re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", cnpj_fornecedor):
        print("CNPJ Inválido!")
        sleep(3)
        sys.exit()
    else:
        print("CNPJ Válido!")   
        sleep(1.5)


def encerrar_sistema():

    os.system('cls')
    print('\033[1;30;44mOBRIGADO POR ESCOLHER A ENGINSTOCK!\033[m')
    sleep(1.2)
    print('\033[1m[1;30mENCERRANDO SISTEMA...\033[m')
    sleep(1.5)
    sys.exit()
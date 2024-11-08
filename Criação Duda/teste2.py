import json
import os

cadastrar_usuario = os.path.join(os.path.dirname(__file__), 'addusuario.json')

if not os.path.exists(cadastrar_usuario):
    with open(cadastrar_usuario, 'w') as f:
        json.dump([], f, indent=4)

with open(cadastrar_usuario, 'r') as f:
    usuario = json.load(f)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

usuario[nome] = 'nome'
usuario[idade] = idade

with open(cadastrar_usuario, 'w') as f:
    json.dump(usuario,f, indent=4)
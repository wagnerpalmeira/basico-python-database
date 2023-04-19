import sqlite3
from functions.usuario_db import insert, listar
from views.tela_inicial import tela_inicial

conn = sqlite3.connect('aula_database') 
c = conn.cursor()

opc = 0

def main():
    global opc
    while(opc != 4):
        print("1 - Inserir novo usuário\n2 - Listar Usuarios")
        opc = int(input("Digite a opção: "))
        
        if opc == 1:
            nome = input("Digite o novo usuário: ")
            senha = input("Digite a nova senha: ")
            insert(conn, [
                nome,
                senha
            ])
        elif opc == 2:
            usuarios = listar(conn)
            for usuario in usuarios:
                print(usuario)

        elif opc == 3:
            tela_inicial()
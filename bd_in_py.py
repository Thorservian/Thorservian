from menu import *
import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXT UNIQUE,
               criado_em TEXT
               )
""")
conn.commit()

def cadastrar_users():
    print("\n === Novo Usuario ===")
    nome = input(f"Nome: ").strip()
    email = input(f"Email: ").strip()

    criado_em = datetime.now().strftime("%d/%m/Y %H:%M")

    try:
        cursor.execute('''
        INSERT INTO users(nome, email, criado_em)
        VALUES(?, ?, ?)
        ''', (nome, email, criado_em))
        print("\nUser {nome} cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("\n Erro: Esse email já está cadastrado!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def listar_users():
    cursor.execute("SELECT id, nome, email, criado_em FROM users")
    users = cursor.fetchall()

    if not users:
        print("\nNenhum users cadastrado ainda.")

    print("\n" + "="*80)
    print(f"{'ID':<4} {'Nome':<20} {'Email':<25} {'Data Cadastro':<20}")
    print("\n" + "="*80)
    for u in users:
        id_, nome, email, data = u
        id_ = str(u[0]) if u[0] is not None else ""
        nome = str(u[1]) if u[1] is not None else ""
        email = str(u[2]) if u[2] is not None else ""
        data = str(u[3]) if u[3] is not None else ""
        print(f"{id_:<4} {nome:<20} {email:<25} {data}")
    print("="*80)

def buscar_users():
    termo = input("\nDigite o nome ou a parte do nome: ").strip()
    cursor.execute("SELECT * FROM users WHERE nome LIKE?", (f"%{termo}%",))
    resultados = cursor.fetchall()

    if resultados:
        print(f"\n{len(resultados)} user(s) encontrado(s):")
        for r in resultados:
            print(f"ID: {r[0]} | {r[1]} | {r[2]} | {r[3]}")
    else:
        print("\nNenhum user encontrado.")

def atualizar_users():
    listar_users()
    try:
        id_user = int(input("\nDigite o ID do user para atualizar: "))

        cursor.execute("SELECT * FROM users WHERE id = ?", (id_user,))
        if not cursor.fetchone():
            print("ID não encontrado!")
            return
        
        print("\nDeixe em branco para manter o valor atual.")
        nome = input(f"Nome: ").strip()
        email = input(f"Email: ").strip()
    
        if nome:
            cursor.execute("UPDATE users SET nome = ? WHERE id = ?", (nome, id_user))
        if email:
            try:
                cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, id_user))
            except sqlite3.IntegrityError:
                print("Erro: Esse email já está sendo usado por outro ususario!")
                return
        conn.commit()
        print("\nCliente atualizado com sucesso!")
    except ValueError:
        print("ID precisa ser um número!")

def deletar_user():
    listar_users()
    try:
        id_user = int(input("\nDigite o ID do usuario para ser deletado:"))
        cursor.execute("DELETE FROM users WHERE id = ?", (id_user,))
        if cursor.rowcount > 0:
            conn.commit()
            print("\nUser deletado com sucesso!")
        else:
            print("\nID não encpntrado!")
    except ValueError:
        print("ID precisa ser um número!")

def menu():
    while True:
        print("\n" + "="*40)
        print("     SISTEMA DE GESTÃO DE USUARIOS      ")
        print("="*40)
        print("1. Cadastrar user")
        print("2. Listar todos")
        print("3. Buscar por nome")
        print("4. Actualizar User")
        print("5. Deletar User")
        print("0. Sair")
        print("="*40)

        op = int(input("Escolha uma opção: ").strip())

        if op == 1:
            cadastrar_users()
        elif op == 2:
            listar_users()
        elif op == 3:
            buscar_users()
        elif op == 4:
            atualizar_users()
        elif op == 5:
            deletar_user()
        elif op == 0:
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida, tente de novo.")

if __name__ == "__main__":
    menu()
    conn.close()
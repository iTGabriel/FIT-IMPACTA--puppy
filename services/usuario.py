import sqlite3
import json


# SELECT DE TODOS OS REGISTROS NO BANCO DE DADOS DA TABELA 'Cliente'
def select_all():
      connection = sqlite3.connect('db_puppy.db')
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM Cliente;")
      resultado = cursor.fetchall()
      cursor.close()
      connection.close()
      return resultado


def buscar_usuario(senha, usuario=None, cpf=None):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cliente WHERE (usuario =:usuario AND senha =:senha ) OR (cpf =:cpf AND senha =:senha)",
    {"usuario":usuario, "senha":senha, "cpf":cpf})
    print(senha, usuario, cpf)
    busca = cursor.fetchone()
    cursor.close()
    connection.close()
    return busca


# INSERT NA TABELA 'Cliente' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome, usuario, senha, cpf, endereco, telefone_residencial, telefone_celular):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Cliente (usuario, senha, cpf, nome, endereco, telefone_residencial, telefone_celular) VALUES (?, ?, ?, ?, ?, ?, ?)"
    # id_usuario = cursor.lastrowid
    cursor.execute(sql, (usuario, senha, cpf, nome, endereco, telefone_residencial, telefone_celular))
    cursor.close()
    connection.commit()
    connection.close()
    return True
    

def update_usuario(nome, usuario, senha, cpf, endereco, telefone_residencial, telefone_celular, id_cliente):
    try:
        connection = sqlite3.connect('db_puppy.db')
        cursor = connection.cursor()

        print(nome, usuario, senha, cpf, endereco, telefone_residencial, telefone_celular, id_cliente)
        update = "UPDATE Cliente SET usuario = ?, senha = ?, cpf = ?, nome = ?, endereco = ?, telefone_residencial = ?, telefone_celular = ? WHERE id_cliente = ?"
        cursor.execute(update, (usuario, senha, cpf, nome, endereco, telefone_residencial, telefone_celular, id_cliente))
        cursor.close()
        connection.commit()
        connection.close()
        return True
    except:
        return False
    




def remover_id(id_usuario):
    try:
        connection = sqlite3.connect('db_puppy.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Cliente WHERE id_cliente = {}".format(id_usuario))
        cursor.close()
        connection.commit()
        connection.close()
        return True
    except:
        return False
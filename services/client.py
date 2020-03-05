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
      print(resultado)
      return resultado


# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID
def busca_por_id(id_Cliente):
    try:
        connection = sqlite3.connect('db_puppy.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cliente WHERE id_cliente = {}".format(id_Cliente))
        busca = cursor.fetchall()
        print(busca)
        cursor.close()
        connection.close()
        return busca
    except:
        return "Falha"
        




# INSERT NA TABELA 'Cliente' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome_cliente, cpf_cliente, endereco_cliente, telefone_residencial_cliente, telefone_celular_cliente):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Cliente (id_cliente, cpf, nome, endereco, telefone_residencial, telefone_celular) VALUES (?, ?, ?, ?, ?, ?)"
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_cliente, cpf_cliente, nome_cliente, endereco_cliente, telefone_residencial_cliente, telefone_celular_cliente))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente


def remover_por_id(id_Cliente):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "DELETE FROM Cliente WHERE id_cliente = {}".format(id_Cliente)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_Cliente))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente
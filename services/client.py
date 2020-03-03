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


# ''''A SER FEITO''' 
# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID
def busca_por_id(idCliente):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM Cliente WHERE id_cliente = {}".format(idCliente)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (idCliente))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente




# INSERT NA TABELA 'Cliente' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome, cpf, endereco, telefone_residencial, telefone_celular):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Cliente (id_cliente, cpf, nome, endereco, telefone_residencial, telefone_celular) VALUES (?, ?, ?, ?, ?, ?)"
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_cliente, cpf, nome, endereco, telefone_residencial, telefone_celular))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente


def remover_por_id(idCliente):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "DELETE FROM Cliente WHERE id_cliente = {}".format(idCliente)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (idCliente))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente
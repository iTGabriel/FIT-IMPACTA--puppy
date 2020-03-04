import sqlite3
import json


# SELECT DE TODOS OS REGISTROS NO BANCO DE DADOS DA TABELA 'Pet_Shop'
def select_all():
      connection = sqlite3.connect('db_puppy.db')
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM Pet_Shop;")
      resultado = cursor.fetchall()
      cursor.close()
      connection.close()
      print(resultado)
      return resultado



# SELECT DOS DADOS DA TABELA 'Pet_Shop' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID
def busca_por_id(id_petshop):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM Pet_Shop WHERE id_petshop = {}".format(id_petshop)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_petshop))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente




# INSERT NA TABELA 'Pet_Shop' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome_petshop, razao_social_petshop, cnpj_petshop, endereco_petshop, telefone_residencial_petshop, telefone_celular_petshop, email_petshop):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Pet_Shop (id_petshop, nome, razao_social, cnpj, endereco, telefone_residencial, telefone_celular, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    id_petshop = cursor.lastrowid
    cursor.execute(sql, (id_petshop, nome_petshop, razao_social_petshop, cnpj_petshop, endereco_petshop, telefone_residencial_petshop, telefone_celular_petshop, email_petshop))
    cursor.close()
    connection.commit()
    connection.close()
    return id_petshop



# REMOVE O REGISTRO DA TABELA 'Pet_Shop' COM BASE NO ID INFORMADO
def remover_por_id(id_petshop):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "DELETE FROM Cliente WHERE id_cliente = {}".format(id_petshop)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_petshop))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente
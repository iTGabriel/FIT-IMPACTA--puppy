import sqlite3
import json


# SELECT DE TODOS OS REGISTROS NO BANCO DE DADOS DA TABELA 'Clinica'
def select_all():
      connection = sqlite3.connect('db_puppy.db')
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM Clinica;")
      resultado = cursor.fetchall()
      cursor.close()
      connection.close()
      print(resultado)
      return resultado



# SELECT DOS DADOS DA TABELA 'Clinica' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID
def busca_por_id(id_clinica):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM Clinica WHERE id_clinica = {}".format(id_clinica)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_clinica))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente



# INSERT NA TABELA 'Clinica' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome_clinica, razao_clinica, cnpj_clinica, endereco_clinica, telefone_residencial_clinica, telefone_celular_clinica, email_clinica):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Clinica (id_clinica, nome, razao_social, cnpj, endereco, telefone_residencial, telefone_celular, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    id_clinica = cursor.lastrowid
    cursor.execute(sql, (id_clinica, nome_clinica, razao_clinica, cnpj_clinica, endereco_clinica, telefone_residencial_clinica, telefone_celular_clinica, email_clinica))
    cursor.close()
    connection.commit()
    connection.close()
    return id_clinica



# REMOVE O REGISTRO DA TABELA 'Clinica' COM BASE NO ID INFORMADO
def remover_por_id(id_clinica):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "DELETE FROM Clinica WHERE id_clinica = {}".format(id_clinica)
    id_cliente = cursor.lastrowid
    cursor.execute(sql, (id_clinica))
    cursor.close()
    connection.commit()
    connection.close()
    return id_cliente
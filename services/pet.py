import sqlite3
import json


# SELECT DE TODOS OS REGISTROS NO BANCO DE DADOS DA TABELA 'Pet'
def select_all():
      connection = sqlite3.connect('db_puppy.db')
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM Pet;")
      resultado = cursor.fetchall()
      cursor.close()
      connection.close()
      print(resultado)
      return resultado


# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID
def busca_por_id(id_pet):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM Pet WHERE id_pet = {}".format(id_pet)
    id_pet = cursor.lastrowid
    cursor.execute(sql, (id_pet))
    cursor.close()
    connection.commit()
    connection.close()
    return id_pet



# INSERT NA TABELA 'Pet' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nome_pet, tipo_pet, sexo_pet, raca_pet, idade_pet, dono_pet):
    try:
        connection = sqlite3.connect('db_puppy.db')
        cursor = connection.cursor()
        sql = "INSERT INTO Pet (id_pet, nome, tipo, sexo, raca, idade, cliente_id,) VALUES (?, ?, ?, ?, ?, ?, ?)"
        id_pet = cursor.lastrowid
        cursor.execute(sql, (id_pet, nome_pet, tipo_pet, sexo_pet, raca_pet, idade_pet, dono_pet))
        cursor.close()
        connection.commit()
        connection.close()
        return id_pet
    except:
        return "Falha em realizar cadastro de pet"



# REMOVE O REGISTRO DA TABELA 'Cliente' COM BASE NO ID INFORMADO
def remover_por_id(id_pet):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "DELETE FROM Pet WHERE id_pet = {}".format(id_pet)
    id_pet = cursor.lastrowid
    cursor.execute(sql, (id_pet))
    cursor.close()
    connection.commit()
    connection.close()
    return id_pet
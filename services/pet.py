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


# ''''A SER FEITO''' 
# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID


# INSERT NA TABELA 'Pet' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nomePET, tipoPET, sexoPET, racaPET, idadePET, donoPET):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Pet (id_pet, nome, tipo, sexo, raca, idade, cliente_id,) VALUES (?, ?, ?, ?, ?, ?, ?)"
    id_pet = cursor.lastrowid
    cursor.execute(sql, (id_pet, nomePET, tipoPET, sexoPET, racaPET, idadePET, donoPET))
    cursor.close()
    connection.commit()
    connection.close()
    return id_pet


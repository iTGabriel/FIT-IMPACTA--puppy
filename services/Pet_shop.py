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


# ''''A SER FEITO''' 
# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID


# INSERT NA TABELA 'Pet_Shop' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nomePET_SHOP, razao_socialPET_SHOP, cnpjPET_SHOP, enderecoPET_SHOP, telefone_residencialPET_SHOP, telefone_celularPET_SHOP, emailPET_SHOP):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Pet_Shop (id_petshop, nome, razao_social, cnpj, endereco, telefone_residencial, telefone_celular, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    id_petshop = cursor.lastrowid
    cursor.execute(sql, (id_petshop, nomePET_SHOP, razao_socialPET_SHOP, cnpjPET_SHOP, enderecoPET_SHOP, telefone_residencialPET_SHOP, telefone_celularPET_SHOP, emailPET_SHOP))
    cursor.close()
    connection.commit()
    connection.close()
    return id_petshop


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


# ''''A SER FEITO''' 
# SELECT DOS DADOS DA TABELA 'X' FILTRANDO POR ID OU 'TEXTO' COMPLETO INFORMADO PELO USUÁRIO ATRAVÉS(SEGUNDA OPÇÃO) DO CAMPO PRINCIPAL/ALTERNATIVO DO ID


# INSERT NA TABELA 'Clinica' UTILIZANDO 'AUTO_INCREMENT' 
def insert_dados(nomeClinica, razaoClinica, cnpjClinica,enderecoClinica, telefone_residencialClinica, telefone_celularClinica, emailClinica):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    sql = "INSERT INTO Clinica (id_clinica, nome, razao_social, cnpj, endereco, telefone_residencial, telefone_celular, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    id_clinica = cursor.lastrowid
    cursor.execute(sql, (id_clinica, nomeClinica, razaoClinica, cnpjClinica, enderecoClinica, telefone_residencialClinica, telefone_celularClinica, emailClinica))
    cursor.close()
    connection.commit()
    connection.close()
    return id_clinica
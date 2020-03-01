import sqlite3 

sql_create = ''' CREATE TABLE Cliente (
    id_cliente integer primary key autoincrement,
    cpf varchar(11) unique,
    nome varchar(50),
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14)
);

CREATE TABLE Pet (
    id_pet integer primary key autoincrement,
    nome varchar(20),1
    tipo varchar(10),
    sexo char(1),
    raca varchar(30),
    idade integer,
    cliente_id integer,
    FOREIGN KEY(cliente_id) REFERENCES Cliente(id_cliente)
   
);

CREATE TABLE Pet_Shop (
    id_petshop integer primary key autoincrement,
    nome varchar(50),
    razao_social varchar(50) unique,
    cnpj varchar(18) unique,
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14),
    email varchar(100)
    
);

CREATE TABLE Clinica (
    id_clinica integer primary key autoincrement,
    nome varchar(50),
    razao_social varchar(50) unique,
    cnpj varchar(18) unique,
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14),
    email varchar(100)

);

CREATE TABLE Consulta (
    id_consulta integer primary key autoincrement,
    clinica_id integer,
    tipo varchar(20),
    pet_id integer,
    dia text,
    horario text,
    cliente_id integer,
    FOREIGN KEY(clinica_id) REFERENCES Clinica(id_clinica),
    FOREIGN KEY(pet_id) REFERENCES Pet(id_pet),
    FOREIGN KEY(cliente_id) REFERENCES Cliente(id_cliente)

);

CREATE TABLE Banho_Tosa (
    petshop_id integer,
    tipo varchar(10),
    pet_id integer,
    dia text,
    horario text,
    cliente_id text,
    FOREIGN KEY(petshop_id) REFERENCES Pet_Shop(id_petshop),
    FOREIGN KEY(pet_id) REFERENCES Pet(id_pet),
    FOREIGN KEY(cliente_id) REFERENCES Cliente(id_cliente)

);

'''

def cria_bd():
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    cursor.executescript(sql_create)
    cursor.close()
    connection.close()

cria_bd()

'''
TIPO da tabela Banho_Tosa refere se vai ser banho ou tosa, ou seja
o serviço. 
TIPO da tabela Pet refere ao tipo de animal.
TIPO da tabela consulta é qual serviço vai ser feito - avaliação, exame,
retorno
'''
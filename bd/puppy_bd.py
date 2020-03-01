import sqlite3 

sql_create = [
    
    ''' CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente integer primary key autoincrement,
    cpf varchar(11) unique,
    nome varchar(50),
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14)
)''',

'''
CREATE TABLE IF NOT EXISTS Pet (
    id_pet integer primary key autoincrement,
    nome varchar(20),
    tipo varchar(10),
    sexo char(1),
    raca varchar(30),
    idade integer,
    cliente_id integer,
    FOREIGN KEY(cliente_id) REFERENCES Cliente(id_cliente)
   
)''',

'''
CREATE TABLE IF NOT EXISTS Pet_Shop (
    id_petshop integer primary key autoincrement,
    nome varchar(50),
    razao_social varchar(50) unique,
    cnpj varchar(18) unique,
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14),
    email varchar(100)
    
)''',

'''
CREATE TABLE IF NOT EXISTS Clinica (
    id_clinica integer primary key autoincrement,
    nome varchar(50),
    razao_social varchar(50) unique,
    cnpj varchar(18) unique,
    endereco varchar(100),
    telefone_residencial varchar(14),
    telefone_celular varchar(14),
    email varchar(100)

)''',

'''
CREATE TABLE IF NOT EXISTS Consulta (
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

)''',

'''
CREATE TABLE IF NOT EXISTS Banho_Tosa (
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

''']

def criar_bd(comando):
    connection = sqlite3.connect('db_puppy.db')
    cursor = connection.cursor()
    cursor.execute(comando)
    cursor.close()
    connection.close()

def criar_muitasTabelas():
    for tabela in sql_create:
        criar_bd(tabela)

# cria_bd()

'''
TIPO da tabela Banho_Tosa refere se vai ser banho ou tosa, ou seja
o serviço. 
TIPO da tabela Pet refere ao tipo de animal.
TIPO da tabela consulta é qual serviço vai ser feito - avaliação, exame,
retorno
'''
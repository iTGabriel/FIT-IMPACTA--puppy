from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import usuario as usuario
from bd import puppy_bd as scriptPUPPYDATABASE
import json

app = Flask(__name__)


## BUSCA TODOS OS REGISTRO DA TABELA CLIENTES
@app.route('/adm/usuarios/listagem/')
def usuario_listagem():
    items = usuario.select_all()
    return render_template('lista_usuarios.html', lista_usuarios = items)


##########################################
############# leirbagti@ #################
##########################################



# ROTA DE INICIO/LOGIN
@app.route('/')
def index():
    return render_template('index.html')


### ROTAS DE USUÁRIO ###

# LOGIN
@app.route('/usuario/login/',  methods=['POST'])
def usuario_login():

    login = request.form['login_usuario']
    senha = request.form['senha_usuario']

    try:
        busca = usuario.buscar_usuario(senha, login)
        if busca != None:
            return render_template('bem_vindo.html', dados_usuario = busca)
    except:
            return "Usuário ou senha errado"


# CADASTRO
@app.route('/usuario/cadastro', methods=['POST'])
def usuario_cadastro():
    
    nome = request.form['nome_usuario']
    login = request.form['nome_login_usuario']
    senha = request.form['senha_usuario']
    cpf = request.form['cpf_usuario']
    endereco = request.form['endereco_usuario']
    telefone = request.form['tel_residencial_usuario']
    celular = request.form['tel_movel_usuario']
    
    try:
        usuario.insert_dados(nome, login, senha, cpf, endereco, telefone, celular)
        try:
            busca = usuario.buscar_usuario(senha, login, cpf)
            return render_template('bem_vindo.html', dados_usuario = busca)
        except:
            return "Falha em realizar busca"
    except:
        return "Falha em realizar cadastro"


# UPDATE/ATUALIZAR
@app.route('/usuario/atualizar', methods=['POST'])
def usuario_atualizar():

    id_usuario = request.form['id_usuario']
    login = request.form['login_usuario']
    senha = request.form['senha_usuario']
    nome = request.form['nome_usuario']
    cpf = request.form['cpf_usuario']
    endereco = request.form['endereco_usuario']
    telefone = request.form['tel_residencial_usuario']
    celular = request.form['tel_movel_usuario']

    try:
        update = usuario.update_usuario(nome, login, senha, cpf, endereco, telefone, celular, id_usuario)
        print(update)
        if update == True:
            return render_template('bem_vindo.html', dados_usuario = [id_usuario, login, senha, nome, cpf, endereco, telefone, celular])
    except:
        return "Falha em atualizar os dados"
    

@app.route('/usuario/delete/', methods=['POST'])
def usuario_remover():
    try:
        id_usuario = request.form['id_usuario']
        exclusao = usuario.remover_id(id_usuario)
        if exclusao == True:
            return usuario_listagem()
    except:
        return "Falha em realizar remoção do usuário."

### FIM ROTAS DE USUÁRIO ###


scriptPUPPYDATABASE.criar_muitasTabelas()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import client as cliente
from bd import puppy_bd as scriptPUPPYDATABASE
import json

app = Flask(__name__)

# ROTAS CLIENTE

## BUSCA DE TODOS OS REGISTRO DA TABELA CLIENTES
@app.route('/clientes')
def clientes():
        return render_template('cadastro_cliente.html')
    # try:
    #     # return cliente.select_all()
    # except:
    #     return "Falha em realizar busca de todos os 'clientes'"

@app.route('/clientes/all')
def clientes_todos():
        items = cliente.select_all()
        dados = {'id': items[0][0], 'nome': items[0][2], 'cpf': items[0][1], 'endereco': items[0][3], 'telefone_residencial': items[0][4], 'telefone_celular': items[0][5]}
        return render_template('dados_cliente.html', lista_clientes = dados)
    # try:
    #     # return cliente.select_all()
    # except:
    #     return "Falha em realizar busca de todos os 'clientes'"


## CADASTRO DE CONTA/1REGISTRO NA TABELA CLIENTE
@app.route('/clientes/cadastro', methods=['POST'])
def clientes_cadastro():
    # O NOME DENTRO DO COLCHETES É O NOME DO CAMPO QUE SERÁ CONSUMIDO DO FRONT-END
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    tel_residencial = request.form['tel_residencial']
    tel_movel = request.form['tel_movel']

    try:
        cliente.insert_dados(nome, cpf, endereco, tel_residencial, tel_movel)
        return render_template('dados_cliente.html', lista_clientes = cliente.select_all())
    except:
        return "Falha em realizar cadastro de clientes"

@app.route('/clientes/buscar-cliente')
def buscar_cliente():
    idCliente = request.args['idCliente']
    try:
        busca = cliente.busca_por_id(idCliente)
        print(busca)
        return busca
    except:
        return "Falha em realizar busca do client pelo id {}".format(idCliente)


### FIM ROAS CLIENTE !!!







scriptPUPPYDATABASE.criar_muitasTabelas()
if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
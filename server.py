from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import client as cliente
from bd import puppy_bd as scriptPUPPYDATABASE
import json

app = Flask(__name__)

# ROTAS DE INDEX/CADASTRO

## BUSCA DE TODOS OS REGISTRO DA TABELA CLIENTES
@app.route('/clientes')
def clientes():
        return render_template('cadastro_cliente.html')



@app.route('/clientes/all')
def clientes_todos():
    try:
        items = cliente.select_all()
    except:
        print("Falha em mostrar os dados de clientes")
        return ''

    return render_template('dados_cliente.html', lista_clientes = items)



@app.route('/clientes/buscar-cliente')
def buscar_cliente():
    idCliente = request.args['idCliente']
    try:
        busca = cliente.busca_por_id(idCliente)
        return busca
    except:
        return "Falha em realizar busca do client pelo id {}".format(idCliente)




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

@app.route('/clientes/select_atualizar_cliente', methods=['POST', 'GET'])
def select_atualizar_cliente():
    try:
        items = cliente.select_all()
    except:
        return "Falha em encontrar o cliente"
    return render_template('update_cliente.html', lista_clientes = items)

@app.route('/clientes/atualizar_cliente', methods=['GET', 'POST'])
def atualizar_cliente():
    dados = request.form['dados_select'].replace("'", "").split(',')
    # try:
    #     resultado = cliente.busca_por_id(idCliente)
    #     resultado = resultado.json(resultado)
    #     print("Resultado -> {}".format(resultado))
    # except:
    #     return "FALHA"
    print(dados)
    return render_template('tela_update_cliente.html', dados_cliente = dados)
    





scriptPUPPYDATABASE.criar_muitasTabelas()
if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
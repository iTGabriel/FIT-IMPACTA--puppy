from flask import Flask, escape, render_template, request, redirect, session, flash, url_for
from services import client as cliente
from bd import puppy_bd as scriptPUPPYDATABASE

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
        print(items)
        return render_template('dados_cliente.html', lista_clientes = items)
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

### FIM OTAS CLIENTE !!!


scriptPUPPYDATABASE.criar_muitasTabelas()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='4811')
    
from crypt import methods
from pickle import NONE
from flask import Flask, render_template, request, redirect , session, flash


class Jogo():
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of war', 'Ação', 'PS4')
jogo3 = Jogo('GTAV', 'Simulação', 'XboxONE')
lista_jogos = [jogo1,jogo2,jogo3]

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def display():

    return render_template('lista.html',titulo='jogos',jogos= lista_jogos)

@app.route('/novo', methods = ['GET', 'POST'])
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect('/')

@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/autenticar',methods=['POST'])
def autenficar():
    if request.form['senha'] == 'toti':
        session['usuario_logado'] = request.form['usuario']
        nome_user = session['usuario_logado']
        flash(f'{nome_user} logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não foi logado com sucesso')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')





app.run(debug=True)

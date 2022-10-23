from crypt import methods
from pickle import NONE
from flask import Flask, render_template, request, redirect , session, flash, url_for


class Jogo():
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of war', 'Ação', 'PS4')
jogo3 = Jogo('GTAV', 'Simulação', 'XboxONE')

lista_jogos = [jogo1,jogo2,jogo3]

class Usuario():
    def __init__(self,nome,username,senha):
        self.nome = nome
        self.username = username
        self.senha = senha

usuario1= Usuario('Eduardo','Barros','2.718')
usuario2= Usuario('Sergio','Sergião','2.718')
usuario3= Usuario('Alan','Math','2.718')

usuarios = {usuario1.nome: usuario1,usuario2.nome: usuario2,usuario3.nome: usuario3,}

app = Flask(__name__)
app.url_map.strict_slashes = False

app.secret_key = 'alura'


@app.route('/')
def display():

    return render_template('lista.html',titulo='jogos',jogos= lista_jogos)

@app.route('/novo', methods = ['GET', 'POST'])
def novo():
    if 'usuario_logado' in session:
        if session['usuario_logado'] != None:
            return render_template('novo.html', titulo='Novo Jogo')
        else:
            return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return redirect(url_for('login', proxima=url_for('novo')))

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect(url_for('display'))

@app.route('/login',methods=['GET', 'POST'])
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/autenticar',methods=['GET','POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.username
            flash(f'{usuario.username} Logado com sucesso')
            proxima_pagina = request.form['proxima']

            return redirect(proxima_pagina)

    else:
        flash('Usuário não foi logado com sucesso')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('display'))





app.run(debug=True)

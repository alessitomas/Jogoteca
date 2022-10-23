from crypt import methods
from flask import Flask, render_template, request, redirect


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


@app.route('/')
def display():

    return render_template('lista.html',titulo='jogos',jogos= lista_jogos)

@app.route('/novo', methods = ['GET', 'POST'])
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar',methods=['GET', 'POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista_jogos.append(jogo)
    return redirect('/')



app.run(debug=True)

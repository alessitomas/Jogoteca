from crypt import methods
from pickle import NONE
from flask import Flask, render_template, request, redirect , session, flash, url_for
from model.sql_alchemy_para_db import db
from model.modelos import UsuarioModel, JogoModel
from flask_admin.contrib.sqla import ModelView
from pathlib import Path
from flask_admin import Admin


FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
rel_arquivo_db = Path('model/VideoGameLibrary.db')
caminho_arq_db = src_folder / rel_arquivo_db

app = Flask(__name__)
admin = Admin(app, name='VideoGameLibrary', template_mode='bootstrap3')
admin.add_view(ModelView(JogoModel, db.session))
admin.add_view(ModelView(UsuarioModel, db.session))

app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = "3.1415926535"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

()


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
    jogo = JogoModel(nome,categoria,console)
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






if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

"""
request -> nos ajuda a pegar informações do formulario

redirect -> é útil para redirecionar para uma determinada página html

session -> é utilizada para armazenar informações específicas do usuário 
            em uma sessão que persiste entre as requisições feitas ao servidor
"""


app = Flask(__name__)
app.secret_key = 'alura'

# Fazendo a conexão com o banco de dados criando uma configuração no app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345678@localhost/jogoteca'

# Instanciando a aplicação do SQLAlchemy
db = SQLAlchemy(app)


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name


@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id) # ver como é isso aqui direito (aula: recuperando a listagem perdida)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    # ver como é isso aqui direito (aula: recuperando a listagem perdida)
    jogo = Jogos.query.filter_by(nome=nome).first() 
    
    if jogo:
        flash('Jogo já existe')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():

    # ver como é isso aqui direito (aula: recuperando a listagem perdida)
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()

    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash(f"{usuario.nickname} logado com sucesso")
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)

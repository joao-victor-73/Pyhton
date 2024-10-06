from flask import Flask, render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Usuarios

"""
request -> nos ajuda a pegar informações do formulario

redirect -> é útil para redirecionar para uma determinada página html

session -> é utilizada para armazenar informações específicas do usuário 
            em uma sessão que persiste entre as requisições feitas ao servidor
"""


@app.route('/')
def index():
    # ver como é isso aqui direito (aula: recuperando a listagem perdida)
    lista = Jogos.query.order_by(Jogos.id)
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


@app.route('/editar/<int:id_jogo>')
def editar(id_jogo):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id_jogo)))
    # fazendo uma query para trazer as informações do banco de dados
    jogo = Jogos.query.filter_by(id=id_jogo).first()
    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    atualizando_jogo = Jogos.query.filter_by(
        id=request.form['id_jogo']).first()
    atualizando_jogo.nome = request.form['nome']
    atualizando_jogo.categoria = request.form['categoria']
    atualizando_jogo.console = request.form['console']

    db.session.add(atualizando_jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id_jogo>')
def deletar(id_jogo):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id_jogo).delete()
    db.session.commit()
    flash("Jogo Deletado com Sucesso!")

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():

    # ver como é isso aqui direito (aula: recuperando a listagem perdida)
    usuario = Usuarios.query.filter_by(
        nickname=request.form['usuario']).first()

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

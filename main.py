from flask import Flask, render_template, request, redirect, flash, url_for
from markupsafe import escape
import sqlite3 as sql
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer
from models.forms import LoginForm
from horaData import t, hoje, simples, Tempo

engine = sqlalchemy.create_engine('sqlite:///db/data.db', echo = False)

Base = declarative_base()
class Tarefas(Base):
    __tablename__= 'tarefas'
    id = Column( Integer, primary_key=True)
    titulo = Column(String(50))
    concluido = Column(String)
    created_at = Column(String)
  
Base.metadata.create_all(engine)




Session = sessionmaker(bind=engine)
session = Session()
query_user = session.query(Tarefas)


app = Flask(__name__)
messages = []

@app.route('/')
def index():
    Session = sessionmaker(bind=engine)
    session = Session()
    tarefas = session.query(Tarefas).order_by(-Tarefas.id)
    
    
    return render_template('home.html', tarefas = tarefas, hoje = int(hoje))

@app.route('/', methods=['POST', 'GET'])
def salvar():
    if request.method == 'POST':
        titulo_text = request.form['titulo']
        if not titulo_text:
            flash( 'O campo tarefa é necessário!', 'danger')
            return redirect(url_for('index'))
        Session = sessionmaker(bind=engine)
        session = Session()
        tarefa = Tarefas(titulo=titulo_text, concluido='false', created_at = simples)
        session.add(tarefa)
        session.commit()
        session.close()
        #flash('Dados inseridos com sucesso.', 'success')
        
        return redirect(url_for('index'))
    return render_template('home.html')

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    tarefa = session.query(Tarefas).filter_by(id=id).first()
    session.delete(tarefa)
    session.commit()
    session.close()
    return redirect(url_for('index'))
        
@app.route('/update/<string:id>', methods=['POST', 'GET'] )
def update(id):
    
    Session = sessionmaker(bind=engine)
    session = Session()
    tarefa = session.query(Tarefas).filter_by(id=id).first()
    if tarefa.concluido == 'false':
        tarefa.concluido='true'
        session.dirty
        session.commit()
    else:
        tarefa.concluido='false'
        session.dirty
        session.commit()
    return redirect(url_for('index')) #redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        return form.username.data
    else:
        flash("Erro", "danger")
    return render_template('register.html', form=form)
    
@app.route('/login', methods= ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return form.username.data
    else:
        flash("erro", "danger")    
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.secret_key='12345'
    app.run(debug=True, host='0.0.0.0', port=8080)
    

import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer

#   Conectando ao DB
engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo = True)

#   Declarando o mapeamento
Base = declarative_base()

class User(Base):
    __tablename__= 'users'
    id = Column( Integer, primary_key=True)
    name = Column(String(50))

#     Criar tabela no DB
Base.metadata.create_all(engine)

#    Criando instâncias da classe
user = User(name='Alexia')

#    Criar uma sessão 
Session = sessionmaker(bind=engine)
session = Session()

#     Adicionar objetos(INSERT)
#session.add(user)
#session.commit()

#   Consultando objetos(SELECT)
#query_user = session.query(User).filter_by(name='Alexia').first()

#   Modificar objetos(UPDATE)
#user.name = "Rodrigo"
#session.dirty
#session.commit()

user = session.query(User).filter_by(name='Alexia').first()
session.delete(user)
session.commit()
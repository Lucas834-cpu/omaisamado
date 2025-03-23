# aqui é aonde vamos adicionar as tabelas do nosso banco de dados
from omaisamado import database, login_menager
from datetime import datetime
from flask_login import UserMixin #passa para a tabela tudo que load_user precisa para encontrar um usuário pela sua chave única

@login_menager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin): # — > abaixo aqui será todas as colunas que queremos dentro do nosso banco
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True) #lazy=true dá-te todas as informações do autor do posto
    #quando se faz um post.autor(isso dá-te tudo sobre o autor do post em questão)
    cursos = database.Column(database.String, nullable=False, default='Não informar')



class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer,  database. ForeignKey('usuario.id'), nullable=False)

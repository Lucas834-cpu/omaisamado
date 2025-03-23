from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, login_user
import os

app = Flask(__name__)
#deoretor é uma função, que atribui a outra função uma nova funcionalidade
#o “app”.route é um 'decoretor' que atribui uma funcionalidade para a função que está logo abaixo dela

#o arquivo "base.html" é um arquivo que será integrado com todas as páginas "html" para que todas tenham a mesma "cara"

app.config['SECRET_KEY']='b5aba2e104289f3ca1b9ce0881671015'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.bd'

bcrypt = Bcrypt(app)
login_menager = LoginManager(app)
login_menager.login_view = 'login_criarconta'
login_menager.login_message_category = 'alert-info'

database = SQLAlchemy(app)

from omaisamado import routes

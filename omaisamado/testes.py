from main import app, database
from omaisamado.models import Usuario, Post

#with app.app_context():
    #database.create_all() #criar banco de dados

#with app.app_context():
    #usuario = Usuario(username='lucas', email='lucas@gmail.com', senha='123456') #para adicionar um usuário no banco de dados
    #database.session.add(usuario) #para adicionar o usuário no banco de dados
    #database.session.commit() #'comitar' as informações dentro do banco de dados, salvamento em definitivo

#with app.app_context():
    #meus_usuarios = Usuario.query.all() # fazer uma pesquisa ono banco de dados de todos os usuário
    #primeiro_usuario = Usuario.query.first() #para pegar o primeiro usuário
    #print(primeiro_usuario.email) #para ver o e-mail do primeiro usuário, por exemplo

#with app.app_context():
    #usuario_teste = Usuario.query.filter_by(id=2).first() # para aplicar filtros numa busca no banco de dado
    ##mas, para pegar o resultado em si e não a query, pois a query retorna-te uma lista, é preciso aplicar um '.first'
    ##ou '.all' para pegar todos que satisfazem o filtro que se aplica

#with app.app_context(): #criando um post na base de dados, muito parecido com a adição de um usuário
    #meu_post = Post(titulo='meu post', id_usuario=1, corpo='lucas que voa')
    #database.session.add(meu_post)
    #database.session.commit()


#with app.app_context():
    #post = Post.query.all() # fazer uma pesquisa ono banco de dados de todos os posts
    #primeiro_usuario = Post.query.first() #para pegar o primeiro post
    #print(post.autor.email) #para ver o post dentro da base de dados e colocando '.autor' pega todas as informações do autor do post
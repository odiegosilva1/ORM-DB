from databese import db, Usuario, Anuncio

#Call Function
db.connect()

db.create_tables([Usuario, Anuncio])

usuario = Usuario.create(nome="jocalino", email="joca@email.com", senha="666555")
usuario = Usuario.create(nome="mariula", email="mariula@email.com", senha="666555")
usuario = Usuario.create(nome="zoio", email="zoio@email.com", senha="666555")

print("Novo usuário:", usuario.id, usuario.nome, usuario.email)


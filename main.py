from databese import db, Usuario, Anuncio

#Call Function
db.connect()

db.create_tables([Usuario, Anuncio])


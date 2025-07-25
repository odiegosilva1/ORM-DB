from peewee import *

db = SqliteDatabase('freelancers.db')


# User Table
class Users(Model):
  name = CharField()
  email = CharField(unique=True)
  pwd = CharField()

  class Metas:
      database = db


# announcement table
class Announcement(Model):
   user = ForeignKeyField(User, backref='users') # type: ignore
   title = CharField()
   description = TextField()
   valor = DecimalField()

   class Meta:
      database = db


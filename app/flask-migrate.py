from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app # we import the app object from the app module
from app import db
'''
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
manager.run()'''
from . import db


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False)
    lastname = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    gender = db.Column(db.String(30),unique=False)
    photo = db.Column(db.String(),nullable=False)
    def __init__(self, firstname, email, lastname, gender, photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.photo = photo
        self.email = email
        self.firstname

    def __repr__(self):
return '<User %r>' % self.username
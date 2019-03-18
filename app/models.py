from . import db
import datetime
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):

    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    gender = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    filename = db.Column(db.String(80))
    #created_date = db.Column(db.Date())
    
    
    def __init__ (self, firstname,lastname,email,location,gender,biography,filename):

        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.biography = biography
        self.email = email
        self.location = location
        self.created_date = created_date
        self.filename = filename
       
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

SECRET_KEY = 'Sup3r$3cretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']="./app/static/uploads"
app.config.from_object(__name__)
from app import views
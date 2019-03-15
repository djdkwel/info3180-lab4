'''from app import app
from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextArea
from wtforms.validators import DataRequired,Email 
from flask_mail import Message'''
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,SelectField,TextAreaField
from wtforms.validators import DataRequired, Email


class UploadForm(FlaskForm):
    firstname = StringField('firstname',validators=[DataRequired()])
    lastname = StringField('lastname',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(),Email()])
    location = StringField('location',validators=[DataRequired()])
    gender = SelectField('gender',choices=[('male', 'Male'),('female', 'Female')])
    biography = TextAreaField('biograpy',validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])


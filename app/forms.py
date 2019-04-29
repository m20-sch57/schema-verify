## -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password =  PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Подтверждение пароля', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class EnterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')    
   
   
class SubmitForm(FlaskForm):
    select_file = FileField('мусОрный текст', validators = [FileRequired()])
    submit = SubmitField('Отправить')

'''
class DownloadStatements(FlaskForm):
    
    
class FileForm(FlaskForm):
    file_title = TextField('Введите текст', validators=[DataRequired()])
    file = FileField("Задача A", validators=[DataRequired()])
    submit = SubmitField('Отправить') 
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length, EqualTo)
from models import User

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with this name already exists.')

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with this email already exists.')

class FormFactory:
    @staticmethod
    def get_form(form_type):
        if form_type == 'login':
            return LoginForm()
        elif form_type == 'register':
            return RegisterForm()
        elif form_type == 'post':
            return PostForm()
        else:
            raise ValueError("Unknown form type: {}".format(form_type))

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, numbers, and underscores only.")
            ),
            name_exists
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class PostForm(FlaskForm):
    content = TextAreaField("What's Up?", validators=[DataRequired()])

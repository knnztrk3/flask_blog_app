from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid Email")])

    password = PasswordField('Password', [InputRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        # if there is a value, then we get the first one there, if there is'nt user then just return None
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        # if there is a value, then we get the first one there, if there is'nt user then just return None
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
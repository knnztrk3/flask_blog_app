from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid Email")])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password  = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
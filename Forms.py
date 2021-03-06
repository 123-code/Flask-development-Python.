from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Password',validators=[DataRequired(),EqualTo('Password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):

    username = StringField('Email',validators = [DataRequired(),Email()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')
    


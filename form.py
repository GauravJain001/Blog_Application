from ast import For
from flask_wtf import Form
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(Form):
    username = StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField("email",validators=[DataRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password",validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField("Sign up")

class LoginForm(Form):
    email = EmailField("email",validators=[DataRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("Log In")

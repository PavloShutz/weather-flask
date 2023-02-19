from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    nickname = StringField("Nickname", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class SignUpForm(LoginForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    submit = SubmitField("Sign Up")

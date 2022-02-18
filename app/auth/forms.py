from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, 
                    ValidationError, BooleanField)
from wtforms.validators import InputRequired, Email, EqualTo
from ..models import User

class SignupForm(FlaskForm):
    name = StringField("Your Name", validators=[InputRequired()])
    username = StringField("Your Username", validators=[InputRequired()])
    email = StringField("Your Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), 
                                EqualTo("password_confirm", message = "Passwords must match")])
    password_confirm = PasswordField("Confirm Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
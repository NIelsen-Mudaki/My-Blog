from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, 
                    ValidationError, BooleanField)
from wtforms.validators import InputRequired, Email, EqualTo
from ..models import User

class SignUpForm(FlaskForm):
    first_name = StringField("Your First Name", validators=[InputRequired()])
    last_name = StringField("Your Last Name", validators=[InputRequired()])
    username = StringField("Your Username", validators=[InputRequired()])
    email = StringField("Your Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), 
                             EqualTo("password_confirm", message = "Passwords must match")])
    password_confirm = PasswordField("Confirm Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up")
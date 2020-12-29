from flask_wtf import FlaskForm
from wtforms import (BooleanField,
            StringField,
            PasswordField,
            SubmitField,
            validators)


class LoginForm(FlaskForm):
    username = StringField('Username')
    passworsd = PasswordField


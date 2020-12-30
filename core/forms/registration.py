from flask_wtf import FlaskForm
from wtforms import (BooleanField,
            StringField,
            PasswordField,
            SubmitField,
            validators)


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4)])
    email = StringField('Email')
    password = PasswordField('Password')
    password2 = PasswordField('Confirm Password',[
                            validators.DataRequired(),
                            validators.EqualTo(
                                'password', message="Passwords must be the same")
    ])
    submit = SubmitField('Submit')

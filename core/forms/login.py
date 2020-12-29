from flask_wtf import FlaskForm
from wtforms import (BooleanField,
            StringField,
            PasswordField,
            SubmitField,
            validators)


class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators.DataRequired()
                            )
    password = PasswordField('Pasword',
                            validators.DataRequired()
                            )

    submit = SubmitField('Submit')
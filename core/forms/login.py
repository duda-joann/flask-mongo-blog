from flask_wtf import FlaskForm
from wtforms import (
            StringField,
            PasswordField,
            SubmitField,
            validators
)


class LoginForm(FlaskForm):
    email = StringField('Email',
                            [validators.DataRequired()]
                            )
    password = PasswordField('Password',
                            [validators.DataRequired()]
                            )

    submit = SubmitField('Submit')

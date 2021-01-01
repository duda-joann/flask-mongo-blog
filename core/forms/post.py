from flask_wtf import FlaskForm
from wtforms import (
            StringField,
            SelectField,
            SubmitField,
            SelectMultipleField,
            FormField,
            validators
)
from core.app import mongo

class NewPostForm(FlaskForm):

    title = StringField('title',
                        [validators.DataRequired])
    body = StringField('contents',
                       [validators.DataRequired])
    published = SelectField('published',
                            choices=['Yes', 'No'],
                            default='Yes')
    tags = FormField('tags',
                            choices=[mongo.db.Tags.find({})],)
    submit = SubmitField('submit')


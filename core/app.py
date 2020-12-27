from flask import Flask
import datetime
from mongoengine import Document
from mongoengine import (DateTimeField,
                         StringField,
                         ReferenceField,
                         ListField,
                         DateField,
                         ObjectIdField,
                         BooleanField)
from flask_pymongo import PyMongo
from core.setting import (connection_string,
                          database_name)


def create_app():
    app = Flask(__name__)
    app.config['MONGO_DBNAME'] = database_name
    app.config['MONGO_URI'] = connection_string
    PyMongo(app)

    return app


class User(Document):
    username = StringField()
    name = StringField()
    email = StringField()
    password = StringField()
    creation_date = DateField(default = datetime.datetime.now())

    def to_json(self):
        return {
            "_id": str(self.pk),
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "creation_date": self.creation_date,
        }


class Post(Document):
    title = StringField()
    body = StringField()
    creation = DateTimeField(default = datetime.datetime.now)
    published = BooleanField()
    tags = ListField(ReferenceField('Tags'))
    author = ListField(ReferenceField('Users'))

    def to_json(self):
        return {
            "post_id": str(self.pk),
            "title": self.title,
            "body": self.body,
            "creation": self.creation,
            "published": self.published,
            "tags": self.tags,
            "author": self.author,

        }


class Tags(Document):
    id = ObjectIdField()
    name = StringField(verbose_name='tag',
                         max_length = 255,
                         required = True,
                         unique= True)
    creation = DateTimeField(default = datetime.datetime.now)

    def to_json(self):
        return {
            "tag_id": self.id,
            "name": self.name,
            "self.creation": self.creation
        }


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

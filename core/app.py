from flask import Flask, render_template
import datetime
from mongoengine import Document
from werkzeug.security import generate_password_hash

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


app = Flask(__name__)
app.config['MONGO_DBNAME'] = database_name
app.config['MONGO_URI'] = connection_string
mongo = PyMongo(app)


class Users(Document):
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

    def generate_hashed_password(self, password):
        return generate_password_hash(password)


class Posts(Document):
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


@app.route("/")
def main_view():
    posts = mongo.db.Posts.find({})
    return render_template('main.html', posts = posts)


@app.route('/register/')
def register_user():
    pass




if __name__ == "__main__":
    app.run(debug=True)



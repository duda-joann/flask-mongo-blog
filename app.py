from flask import Flask
from flask_mongoengine import MongoEngine
import datetime


app = Flask(__name__)
app.config['MONGO_DBNAME']= 'blog'
app.config['MONGO_URI'] = "mongodb+srv://root:root1234@cluster0.qabhw.mongodb.net/<dbname?retryWrites=true&w=majority"
db = MongoEngine(app)



class User(db.Document):
    id = db.ObjectsID()
    name = db.StringField()
    email = db.StringField()
    password = db.StringField
    creation_date=db.DateTime(default = datetime.datetime.now())


class Post(db.Document):
    id = db.ObjectsID()
    title = db.StringField(255)
    body = db.StringField()
    creation = db.DateTimeField(default = datetime.datetime.now)
    published = db.BooleanField()
    tags = db.ListField(db.ReferenceField('Tag'))
    author = db.ListField(db.ReferenceField('Users'))



class Tags(db.Document):
    name = db.StringFiel(verbose_name='tag',
                         max_length = 255,
                         required = True,
                         unique= True)
    creation = db.DateTimeField(default = datetime.datetime.now)



if __name__ == "__main__":
    app.run(debug=True)
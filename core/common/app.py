from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    #app.config['MONGO_URI'] = "mongodb+srv://root:root1234@cluster0.qabhw.mongodb.net/<blog>?retryWrites=true&w=majority"
    app.config['MONGODB_SETTINGS'] = {
            'db': 'blog',
            'host':"cluster0.qabhw.mongodb.net",
            'username': 'root',
            'password': 'root1234'
        }
    SECRET_KEY = 'nojeszczeczego?!?!'
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)

    return app





from flask import Flask
from .db import db


def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
            'db': 'blog',
            'host': 'localhost',
            'username': 'root',
            'password': 'root1234'
        }
    SECRET_KEY = 'nojeszczeczego?!?!'
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)


    return app





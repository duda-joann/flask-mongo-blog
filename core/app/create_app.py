from flask import Flask
from flask_pymongo import PyMongo
from db import mongo

def create_app():
    app = Flask(__name__)
    app.config['MONGO_DBNAME'] = 'blog'
    app.config['MONGO_URI'] = "mongodb+srv://root:root1234@cluster0.qabhw.mongodb.net/<dbname?retryWrites=true&w=majority"

    return app

if __name__ == "__main__":
    app = create_app()
    app = mongo(app)



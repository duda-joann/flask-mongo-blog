from functools import wraps
from flask import Flask, render_template, jsonify, session, redirect, request
import datetime
import pymongo
from typing import Callable
from mongoengine import (DateTimeField,
                         StringField,
                         ReferenceField,
                         ListField,
                         DateField,
                         ObjectIdField,
                         BooleanField)
from flask_pymongo import PyMongo
from forms.registration import RegistrationForm
from forms.login import LoginForm
from models.users import Users
from app.create_app import app
from app.db import mongo


@app.route('/user/signup/', methods=['POST'])
def signup():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        return Users.signup()
    else:
        return render_template('registration.html', form=form)

@app.route('/user/signout/')
def signout():
    return Users().signout()


@app.route('/user/login', methods= ['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        return Users.login()

    return render_template('login.html', form=form)

def login_required(function:Callable) ->Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return function(*args, **kwargs)
        else:
            redirect('/')
    return wrapper


@app.route("/")
def main_view():
    posts = mongo.db.Posts.find({})
    return render_template('main.html', posts = posts)


@app.route('/dashboard/')
@login_required
def generate_dashboard():
    return render_template('navigation.html')


if __name__ == "__main__":
    app.run(debug=True)




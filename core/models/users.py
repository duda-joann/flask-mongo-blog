from flask import (jsonify,
                   request,
                   session,
                   redirect)
import datetime

from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from core.common.db import db


class Users(db.Document):
    username = db.StringField()
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    creation_date = db.DateField(default = datetime.datetime.now())

    def start_session(self, user):
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200


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

    def check_hashed_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    def signup(self):

        user = {
            "username": request.form['username'],
            "name": request.form['name'],
            "email": request.form['email'],
            "password": request.form['password'],
        }

        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "email address already exists"}), 400

        if db.users.find_one({"username": user['username']}):
            return jsonify({"error": "email address already exists"}), 400

        user["password"] = self.generate_hashed_password(user["password"])

        if db.users.insert_one(user):
            self.start_session(user)
            return self.start_session(user), jsonify({"message": "success"}), 200

        return jsonify({"error": "registration not posible"}), 400


    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.users.find_one({"email": email})

        if self.check_hashed_password(user['password'], password):
            return self.start_session(user)
        return redirect('/')



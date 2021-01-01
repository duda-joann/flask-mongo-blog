from flask import jsonify, session, redirect, request
import datetime
from mongoengine import Document
from mongoengine import (DateTimeField,
                         StringField,
                         ReferenceField,
                         ListField,
                         BooleanField)
from core.common.db import db
from .users import Users


class Posts(db.Document):
    title = db.StringField()
    body = db.StringField()
    creation = db.DateTimeField(default=datetime.datetime.now)
    published = db.BooleanField()
    tags = db.ListField(ReferenceField('Tags'), default= [])
    author = db.ReferenceField(Users)

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

    def get_all_posts(self):
        posts = db.Posts.find({}).sort('creation')
        if posts:
            return posts
        return jsonify({"message": "There is no posts available"})

    def get_post(self, id):
        post = db.posts.find_one({'post_id': id})
        if post:
            return post
        return jsonify({"error": "post does not exist"}), 404

    def create_post(self):
        post = {
            'title': request.form['title'],
            'body': request.form['body'],
            'published': request.form['published'],
            'tags': [tag for tag in request.form['tags']],
            'author': session['email'],
        }

        if db.posts.insert_one(post):
            return jsonify({'message', 'Post added successfully'}), 201

        return redirect('/'),

    def update_post(self, id):
        post = db.posts.get_post(id)
        if post.author == session['email']:
            return jsonify({"error":"Hey Guy, it is not your post, you can not update"}), 403

        post = {
            'title': request.form['title'],
            'body': request.form['body'],
            'published': request.form['published'],
            'tags': [tag for tag in request.form['tags']],
            'author': session['email'],
        }

        if db.posts.update(post):
            return jsonify({'message':'Post updated successfully'}), 201

        return redirect('/')

    def delete_post(self, id):
        post = self.get_post(id)
        db.posts.remove(post).first()
        return jsonify({"message": "Post was deleted"}), 404



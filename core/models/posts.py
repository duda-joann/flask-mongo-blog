from bson import ObjectId
from flask import (
                jsonify,
                session,
                redirect,
                request)
import datetime
from mongoengine import (
                         ReferenceField,
                         )
from flask_mongoengine import BaseQuerySet
from marshmallow import (Schema,
                         fields)

from core.common.db import db
from .users import Users, UserSchema
from .comment import Comments, CommentsSchema
from .tags import Tags, TagsSchema


class Posts(db.Document):
    title = db.StringField()
    body = db.StringField()
    creation = db.DateTimeField(default=datetime.datetime.now)
    published = db.BooleanField()
    tags = db.ListField(ReferenceField(Tags), default= [])
    author = db.ReferenceField(Users)
    comments = db.ListField(db.EmbeddedDocumentField(Comments))
    meta = {'collection': 'posts', 'queryset_class': BaseQuerySet}

    @staticmethod
    def get_all_posts():
        posts = Posts.objects().order_by('-creation')
        if posts:
            return posts
        return jsonify({"message": "There is no posts available"})

    def get_posts_by_tag(self, tag: str):
        posts = Posts.objects().get(tags=tag)
        if posts:
            return posts
        return jsonify({"message": "no post available"})

    def get_post(self, id):
        post = Posts.objects.get_or_404(id=id)
        if post:
            return post
        return jsonify({"error": "post does not exist"}), 404

    @staticmethod
    def create_post():
        if request.method == 'POST':
            post = Posts(
                title = request.form['title'],
                body = request.form['body'],
                published = request.form['published'],
                tags = [tag for tag in request.form['tags']],
                author =session['email'],
            )

            if post.save():
                return jsonify({'message', 'Post added successfully'}), 201

            return redirect('/'),

    def update_post(self, id):
        post = self.get_post(id)

        if post.author == session['email']:
            return jsonify({"error":"Hey Guy, it is not your post, you can not update"}), 403

        if request.method == 'POST':
            post = Posts(
                title = request.form['title'],
                body = request.form['body'],
                published = request.form['published'],
                tags= [tag for tag in request.form['tags']],
                author= session['email'],
            )

            if post.update(id=id):
                return jsonify({'message':'Post updated successfully'}), 201
            return redirect('/')

    def delete_post(self, id):
        post = self.get_post(id)
        if post:
            Posts.delete(id=id).first()
            return jsonify({"message": "Post was deleted"}), 404
        return jsonify({"message": "Post not found"}), 404


class PostsSchema(Schema):
    Schema.TYPE_MAPPING[ObjectId] = fields.String
    title = fields.Str()
    body = fields.Str()
    creation = fields.Date()
    published = fields.Boolean()
    tags = fields.List(fields.Nested(TagsSchema))
    author = fields.Nested(UserSchema)
    comments = fields.Nested(CommentsSchema)


post_schema = PostsSchema()
posts_schema = PostsSchema(many=True)


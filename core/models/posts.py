from functools import wraps
from flask import Flask, render_template, jsonify, session, redirect
import datetime
from mongoengine import Document
from mongoengine import (DateTimeField,
                         StringField,
                         ReferenceField,
                         ListField,
                         BooleanField)
from core.common.db import mongo


class Posts(Document):
    title = StringField()
    body = StringField()
    creation = DateTimeField(default=datetime.datetime.now)
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

    def get_posts(self):
        return mongo.db.Posts.find({})

    def create_post(self):
        pass

    def update_posts(self):
        pass

    def delete_post(self):
        pass


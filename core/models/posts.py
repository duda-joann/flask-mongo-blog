from functools import wraps
from flask import Flask, render_template, jsonify, session, redirect
import datetime
from mongoengine import Document
from werkzeug.security import generate_password_hash
import pymongo
from typing import Callable
from mongoengine import (DateTimeField,
                         StringField,
                         ReferenceField,
                         ListField,
                         DateField,
                         ObjectIdField,
                         BooleanField)
from core.common.db import mongo

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



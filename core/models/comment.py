from bson import ObjectId
import datetime
from core.common.db import db
from flask_mongoengine import BaseQuerySet
from marshmallow import (Schema,
                         fields)


class Comments(db.EmbeddedDocument):
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=60)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    text = db.StringField()

    meta = {'collection': 'tags', 'queryset_class': BaseQuerySet}


class CommentsSchema(Schema):
    Schema.TYPE_MAPPING[ObjectId] = fields.String
    name = fields.Str()
    email = fields.Str()
    created_at = fields.Date()
    text = fields.Str()


comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)


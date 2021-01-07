from bson import ObjectId
import datetime
from flask import jsonify
from flask_mongoengine import BaseQuerySet
from core.common.db import db
from marshmallow import (Schema,
                         fields)


class Tags(db.Document):
    id = db.ObjectIdField()
    name = db.StringField(verbose_name='tag',
                         max_length = 255,
                         required = True,
                         unique= True)
    creation = db.DateTimeField(default = datetime.datetime.now)

    meta = {'collection': 'tags', 'queryset_class': BaseQuerySet}

    #added back,  should be used.

    def get_all_tags(self):
        tags = Tags.objects().all()
        if tags:
            return jsonify(tags)
        return jsonify({"message": "There is no tags. Please add some tags"})


class TagsSchema(Schema):
    Schema.TYPE_MAPPING[ObjectId] = fields.String
    name = fields.Str()
    creation = fields.Date()


tag = TagsSchema()
tags = TagsSchema(many=True)


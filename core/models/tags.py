
import datetime
from flask import jsonify
from flask_mongoengine import BaseQuerySet
from core.common.db import db

class Tags(db.Document):
    id = db.ObjectIdField()
    name = db.StringField(verbose_name='tag',
                         max_length = 255,
                         required = True,
                         unique= True)
    creation = db.DateTimeField(default = datetime.datetime.now)

    meta = {'collection': 'tags', 'queryset_class': BaseQuerySet}

    #added back,  should be used.
    def to_json(self):
        return {
            "tag_id": self.id,
            "name": self.name,
            "self.creation": self.creation
        }

    def get_all_tags(self):
        tags = Tags.objects().all()
        if tags:
            return jsonify(tags)
        return jsonify({"message": "There is no tags. Please add some tags"})


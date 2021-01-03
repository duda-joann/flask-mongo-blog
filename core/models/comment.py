import datetime
from core.common.db import db
from flask_mongoengine import BaseQuerySet


class Comments(db.Document):
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=60)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    text = db.StringField()

    meta = {'collection': 'tags', 'queryset_class': BaseQuerySet}




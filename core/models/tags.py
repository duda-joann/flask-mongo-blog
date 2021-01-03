import pymongo
import datetime
from mongoengine import Document
from mongoengine import (
                        DateTimeField,
                        StringField,
                        ObjectIdField,
                        )
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


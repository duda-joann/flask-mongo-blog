import pymongo
import datetime
from mongoengine import Document
from mongoengine import (
                        DateTimeField,
                        StringField,
                        ObjectIdField,
                        )
from core.app import mongo


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


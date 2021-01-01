import datetime
from core.common.db import db

class Comment(db.Document):
    name = db.StringField(max_length=50)
    email = db.StringField(max_length=60)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    text = db.StringField()

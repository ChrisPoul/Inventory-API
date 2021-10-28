import mongoengine as me
from datetime import datetime


class Product(me.Document):
    id = me.IntField(primary_key=True)
    name = me.StringField(required=True)
    price = me.FloatField(default=0)
    time_created = me.DateTimeField(default=datetime.now)
    time_updated = me.DateTimeField(default=datetime.now)

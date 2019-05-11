from peewee import *
from model.base import BaseModel


class Server(BaseModel):
    name = CharField(max_length=200)
    host = CharField(max_length=100, null=False)
    password = CharField(max_length=200, null=False)
    projectDir = CharField(max_length=200, null=False)
    isOnline = IntegerField(default=0)
    status = IntegerField(default=1)
    addTime = DateTimeField(null=True)

    class Meta:
        table_name = 'server'


class User(BaseModel):
    username = CharField(max_length=32, null=False)
    password = CharField(max_length=200, null=False)

    class Meta:
        table_name = 'user'
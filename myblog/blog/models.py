from django.db import models
from django.db import connection

# Create your models here.

class angelo_db(object):
    cursor = connection.cursor()
    def __init__(self):
        pass
        # self.cursor = connection.cursor()

    @classmethod
    def query_one(cls,sql=''):
        cls.cursor.execute(sql)
        return cls.cursor.fetchone()

    @classmethod
    def query_all(cls,sql=''):
        cls.cursor.execute(sql)
        return cls.cursor.fetchall()

    @classmethod
    def query(cls,sql=''):
        cls.cursor.execute(sql)
        return cls.cursor.fetchall()

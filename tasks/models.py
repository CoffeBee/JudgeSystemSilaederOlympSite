from django.db import models
import hashlib
import time
from django.contrib.auth.models import User
from django.db.models import PROTECT

# Create your models here.

class TaskProgramming(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)
    statement = models.FileField(upload_to='tasks/statement/')
class TaskMathematics(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    answer = models.CharField(max_length=20, default='1')
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)
    type = models.IntegerField(default=0)
    judge = models.ForeignKey(User, on_delete=PROTECT, default=1)
    statement = models.FileField(upload_to='tasks/statement/math', default='tasks/statement/7bbb0bd4934ded248d83051a33c986')
class TaskCTF(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    answer = models.CharField(max_length=20, default='1')
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)
    statement = models.FileField(upload_to='tasks/statement/math', default='tasks/statement/7bbb0bd4934ded248d83051a33c986')

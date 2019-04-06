from django.db import models
import hashlib
import time
# Create your models here.

class TaskProgramming(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)
class TaskMathematics(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)
class TaskCTF(models.Model):
    def create_hash():
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:-10]
    title = models.CharField(max_length=200)
    level = models.IntegerField()
    hash_link = models.CharField(max_length=200, default=create_hash)

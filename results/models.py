from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import PROTECT


class MathScore(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT)
    score = models.IntegerField()
    pluser = models.IntegerField()

class ProgScore(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT)
    score = models.IntegerField()
    pluser = models.IntegerField()


class CTFScore(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT)
    score = models.IntegerField()
    pluser = models.IntegerField()

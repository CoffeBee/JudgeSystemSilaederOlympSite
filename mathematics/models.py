from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskMathematicsPurchases(models.Model):
    username = models.CharField(default='CoffeBee', max_length=100)
    item_level = models.IntegerField(default=1)
    item_type = models.CharField(max_length=200)
class MathSubmits(models.Model):
    username = models.CharField(default='CoffeBee', max_length=100)
    answer = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    verdict = models.CharField(max_length=10)
    judge = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    level = models.IntegerField(default=1)
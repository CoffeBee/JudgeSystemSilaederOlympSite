from django.db import models

# Create your models here.

class TaskCTFPurchases(models.Model):
    userid = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.CharField(max_length=200)
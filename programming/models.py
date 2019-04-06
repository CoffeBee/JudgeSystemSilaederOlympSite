from django.db import models

# Create your models here.

class TaskProgrammingPurchases(models.Model):
    userid = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.CharField(max_length=200)

class ProgrammingSubmits(models.Model):
    codeforcesSubmitId = models.IntegerField()
    username = models.CharField(default='CoffeBee', max_length=200)
    task_id = models.IntegerField()
    verdict = models.CharField(max_length=200)
    programmingLanguage = models.CharField(max_length=200)
    timeConsumedMillis = models.IntegerField()
    memoryConsumedBytes = models.IntegerField()




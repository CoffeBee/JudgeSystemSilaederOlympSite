from django.contrib import admin
from .models import TaskProgramming, TaskCTF, TaskMathematics
# Register your models here.


admin.site.register(TaskProgramming)
admin.site.register(TaskCTF)
admin.site.register(TaskMathematics)
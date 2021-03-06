# Generated by Django 2.1.7 on 2019-04-19 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_taskmathematics_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskctf',
            name='answer',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='taskctf',
            name='judge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskctf',
            name='statement',
            field=models.FileField(default='tasks/statement/7bbb0bd4934ded248d83051a33c986', upload_to='tasks/statement/math'),
        ),
    ]

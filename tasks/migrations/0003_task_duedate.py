# Generated by Django 4.1.7 on 2023-03-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='duedate',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]

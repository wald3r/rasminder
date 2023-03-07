from django.db import models

# Create your models here.


class Task(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    taskname = models.CharField(max_length=255)
    tasklist = models.CharField(max_length=255)
    duedate = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.id} {self.taskname} {self.tasklist} {self.duedate}"
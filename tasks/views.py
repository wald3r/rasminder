from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Task

from tasks.services.googleTasksService import googleTasksService

# Create your views here.


def tasks(request):
        googleTasks = googleTasksService().getAllTasks()
        Task.objects.all().delete()
        for x in googleTasks:
                task = Task(id=x[1], taskname=x[0], tasklist=x[2], duedate=x[3])
                task.save()
        dbTasks = Task.objects.all().values()
        template = loader.get_template('main.html')
        context = {
                'alltasks': dbTasks,
        }
        return HttpResponse(template.render(context, request))

def deleteTask(request, id):
        task = get_object_or_404(Task, pk=id)
        googleTasksService().closeTask(task.tasklist, id)
        task.delete()
        return redirect('tasks')



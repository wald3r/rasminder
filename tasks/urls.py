from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('delete/<str:id>', views.deleteTask, name='deleteTask')
]
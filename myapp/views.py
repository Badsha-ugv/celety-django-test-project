from django.shortcuts import render
from django.http import HttpResponse
from .tasks import my_task

def index(request):
    my_task.delay(1, 5)
    return HttpResponse("Task triggered")

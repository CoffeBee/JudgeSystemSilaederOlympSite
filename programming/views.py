from django.shortcuts import render
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from tasks.models import TaskProgramming

def programming(request):
    return render(request, 'programming.html')

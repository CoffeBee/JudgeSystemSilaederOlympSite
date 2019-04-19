from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render, redirect

from JudgeSystemSilaederOlymp.wsgi import scoreViewer
from .models import TaskProgramming, TaskMathematics

# Create your views here.
def statement(request, statement_hash):
    import os
    scoreViewer.UpdateProg()
    import requests

    print(os.path.dirname(os.path.abspath(__file__)))
    try:
        filename = TaskProgramming.objects.filter(hash_link=statement_hash)[0].statement.path
        return FileResponse(open(filename, 'rb'), content_type='application/jpg')
    except Exception as e:
        print(e)
        try:
            filename = TaskMathematics.objects.filter(hash_link=statement_hash)[0].statement.path
            return FileResponse(open(filename, 'rb'), content_type='application/jpg')
        except Exception as e:
            print(e)
            return redirect('../../../')


def setstd(request):
    scoreViewer.setToStd()
    return HttpResponse('ok')


def updateProg(request):
    scoreViewer.UpdateProg()
    return HttpResponse('ok')
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from JudgeSystemSilaederOlymp.wsgi import scoreViewer
# Create your views here.
def statement(request, statement_hash):
    import os
    scoreViewer.UpdateProg()
    import requests

    print(os.path.dirname(os.path.abspath(__file__)))
    try:

        return FileResponse(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/statements/' + statement_hash + '.pdf'), 'rb'))
    except:
        raise Http404("Task doesn't exist")
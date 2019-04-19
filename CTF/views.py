from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from tasks.models import TaskCTF
from results.models import CTFScore
from .models import TaskCTFPurchases
from .models import CTFSubmits
from django.contrib.auth.models import User
from .forms import SubmitForrm
import json
from django.views.decorators.csrf import csrf_exempt

def ctf(request):
    if (request.user.is_authenticated):
        tasks = TaskCTF.objects.all()
        pur = []
        res = []
        alp = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in tasks:
            task = [alp[i.level - 1], i.title, int(i.level / 3 + 1) * 500, int(i.level / 3 + 1) * 100,
                    int(i.level / 3 + 1) * 125, int(i.level / 3 + 1) * 125, i.level]
            if (CTFSubmits.objects.filter(username=request.user.username, verdict="OK", level=i.level).exists()):
                task.append("rgb(30, 124, 52)")
            elif (CTFSubmits.objects.filter(username=request.user.username, verdict="WA", level=i.level).exists()):
                task.append("rgb(225,0,0)")
            else:
                task.append("rgb(255, 255, 255)")
            if (TaskCTFPurchases.objects.filter(username=request.user.username, item_type="CTF", item_level=i.level +1)):
                pur.append([True, i.hash_link])
            else:
                pur.append([False, ''])
            res.append(task)

        form  = SubmitForrm(None)
        level = 0
        if (request.method == 'POST'):
            print([i for i in request.POST.lists()])
            posted = dict([i for i in request.POST.lists()])
            for i in posted.keys():
                posted[i] = posted[i][0]
            level = posted['level']
            del posted['level']
            form = SubmitForrm(posted)
        if form.is_valid():
            print(level)
            answer = form.cleaned_data.get('answer')
            Task = TaskCTF.objects.get(level=int(level))
            if (Task.answer == answer):
                NewSubmit = CTFSubmits(username=request.user.username, answer=answer,
                                       verdict="OK", level=level)
                NewSubmit.save()
            else:
                NewSubmit = CTFSubmits(username=request.user.username, answer=answer,
                                       verdict="WA", level=level)
                NewSubmit.save()

            return redirect('.')


        return render(request, 'CTF.html', context={'tasks': res, 'pur' : pur, 'form' : form})
    else:
        return redirect('../')


def purchases(request, level):
    if (request.user.is_authenticated):
        user = request.user
        username = request.user.username
        ScoreObject = CTFScore.objects.get(user=user)
        ScoreObject.score -= (level + 1) // 3 * 100
        ScoreObject.save()
        Newpurchase = TaskCTFPurchases(username=username, item_level=level + 1, item_type='CTF')
        Newpurchase.save()

    return redirect('../../../')

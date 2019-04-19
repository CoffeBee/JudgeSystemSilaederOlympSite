from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from tasks.models import TaskProgramming
from results.models import ProgScore
from programming.models import TaskProgrammingPurchases
from django.contrib.auth.models import User
def programming(request):
    if (request.user.is_authenticated):
        tasks = TaskProgramming.objects.all()
        pur = []
        res = []
        alp = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in tasks:
            task = [alp[i.level - 1], i.title, int(i.level / 3 + 1) * 500, int(i.level / 3 + 1) * 100,
                    int(i.level / 3 + 1) * 125, int(i.level / 3 + 1) * 125, i.level]
            if (TaskProgrammingPurchases.objects.filter(username=request.user.username, item_type="programming", item_level=i.level +1)):
                pur.append([True, i.hash_link])
            else:
                pur.append([False, ''])
            res.append(task)
        print(pur)
        return render(request, 'programming.html', context={'tasks': res, 'pur' : pur})
    else:
        return redirect('../')


def purchases(request, level):
    if (request.user.is_authenticated):
        user = request.user
        username = request.user.username
        ScoreObject =  ProgScore.objects.get(user=user)
        ScoreObject.score -= (level + 1) // 3 * 100
        ScoreObject.save()
        Newpurchase = TaskProgrammingPurchases(username=username, item_level=level + 1, item_type='programming')
        Newpurchase.save()

    return redirect('../../../')
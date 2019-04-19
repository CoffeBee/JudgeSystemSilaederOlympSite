from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
from tasks.models import TaskMathematics
from results.models import MathScore
from mathematics.models import TaskMathematicsPurchases
from mathematics.models import MathSubmits
from django.contrib.auth.models import User
from .forms import SubmitForrm
import json
from django.views.decorators.csrf import csrf_exempt

def math(request):
    if (request.user.is_authenticated):
        tasks = TaskMathematics.objects.all()
        pur = []
        res = []
        alp = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in tasks:
            task = [alp[i.level - 1], i.title, int(i.level / 3 + 1) * 500, int(i.level / 3 + 1) * 100,
                    int(i.level / 3 + 1) * 125, int(i.level / 3 + 1) * 125, i.level]
            if (MathSubmits.objects.filter(username=request.user.username, verdict="OK", level=i.level).exists()):
                task.append("rgb(30, 124, 52)")
            elif (MathSubmits.objects.filter(username=request.user.username, verdict="PD", level=i.level).exists()):
                task.append("rgb(225,255,0)")
            elif (MathSubmits.objects.filter(username=request.user.username, verdict="WA", level=i.level).exists()):
                task.append("rgb(225,0,0)")
            else:
                task.append("rgb(255, 255, 255)")
            if (TaskMathematicsPurchases.objects.filter(username=request.user.username, item_type="math", item_level=i.level +1)):
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
            description = form.cleaned_data.get('description')
            Task = TaskMathematics.objects.get(level=int(level))
            if (Task.type == 0):
                if (Task.answer==answer):
                    NewSubmit = MathSubmits(username=request.user.username, description=description, answer=answer, verdict="OK", level=level)
                    NewSubmit.save()
                else:
                    NewSubmit = MathSubmits(username=request.user.username, description=description, answer=answer, verdict="WA", level=level)
                    NewSubmit.save()
            else:
                if (Task.answer==answer):
                    NewSubmit = MathSubmits(username=request.user.username, description=description, answer=answer, verdict="PD", judge=Task.judge, level=level)
                    NewSubmit.save()
                else:
                    NewSubmit = MathSubmits(username=request.user.username, description=description, answer=answer, verdict="WA", level=level)
                    NewSubmit.save()

            return redirect('.')


        return render(request, 'math.html', context={'tasks': res, 'pur' : pur, 'form' : form})
    else:
        return redirect('../')


def purchases(request, level):
    if (request.user.is_authenticated):
        user = request.user
        username = request.user.username
        ScoreObject =  MathScore.objects.get(user=user)
        ScoreObject.score -= (level + 1) // 3 * 100
        ScoreObject.save()
        Newpurchase = TaskMathematicsPurchases(username=username, item_level=level + 1, item_type='math')
        Newpurchase.save()

    return redirect('../../../')

def judge(request):
    if (request.user.is_authenticated):
        if (request.user.is_superuser):
            Submits = MathSubmits.objects.filter(verdict='PD', judge=request.user)
            href = []
            for i in Submits:
                href.append(str(i.id))
            return render(request, 'judge_math.html', context={'hrefs': href})

        else:
            redirect('../')
    else:
        redirect('../../')
@csrf_exempt
def judge_task(request, submit_id):
    if (request.user.is_authenticated):
        if (request.user.is_superuser):
            Submit = MathSubmits.objects.get(id=submit_id)
            if (request.method == 'POST'):
                if ('ok' in dict(request.POST.lists())):
                    Submit.verdict = 'OK'
                    Submit.save()
                    return redirect("../")
                else:
                    Submit.verdict = 'WA'
                    Submit.save()
                    return redirect("../")

            return render(request, 'judge_math_task.html', context={'description' : Submit.description})
        else:
            redirect('../')
    else:
        redirect('../../')
import random
import threading
import time
import hashlib
import requests
from .codeforcesApi import call
from .models import CTFScore, MathScore, ProgScore
from programming.models import ProgrammingSubmits
import sys
import json
from django.contrib.auth.models import User

class ScoreUpdate():
    def __init__(self, CTFstdScore, MathstdScore, ProgstdScore, CTFstdPlusser, MathstdPlusser, ProgstdPlusser, apiKey, apiSecret, contestId):
        self.CTFstdScore = CTFstdScore
        self.MathstdScore = MathstdScore
        self.ProgstdScore = ProgstdScore
        self.CTFstdPlusser = CTFstdPlusser
        self.MathstdPlusser = MathstdPlusser
        self.ProgstdPlusser = ProgstdPlusser
        self.lastSubmitId = 1
        self.contestId = contestId
        self.apiKey = apiKey
        self.apiSecret = apiSecret

    def setToStd(self):
        for i in CTFScore.objects.all():
            i.score = self.CTFstdScore
            i.pluser =  self.CTFstdPlusser

        for i in MathScore.objects.all():
            i.score = self.MathstdScore
            i.pluser = self.MathstdPlusser

        for i in ProgScore.objects.all():
            i.score = self.ProgstdScore
            i.pluser = self.ProgstdPlusser

    def startMonitor(self, timeInterval, lastSubmitId, contestId):
        self.MonitorThread = threading.Thread(target=self.Monitor, args=(timeInterval, lastSubmitId, contestId,))
        self.MonitorThread.run()

    def Update(self):
        self.UpdateProg()
        self.UpdateMath()
        self.UpdateCTF()

    def UpdateProg(self):
        print("fuck")

        newSubmits = call('contest.status', lastSubmit=self.lastSubmitId, key=self.apiKey, secret=self.apiSecret, contestId=self.contestId)

        if (newSubmits == "Codeforces Api error"):
            sys.exit('Codeforces Api error')
        else:
            self.lastSubmitId += len(newSubmits)

            for submit in newSubmits:
                submit['problem']['index'] = ord(submit['problem']['index']) - ord('A') + 1
                submitObject = ProgrammingSubmits(codeforcesSubmitId=int(submit['id']),
                                                  username=submit['author']['members'][0]['handle'],
                                                  task_id=submit['problem']['index'],
                                                  verdict=submit['verdict'],
                                                  programmingLanguage=submit['programmingLanguage'],
                                                  timeConsumedMillis=submit['timeConsumedMillis'],
                                                  memoryConsumedBytes=submit['memoryConsumedBytes'])
                if (submit['verdict'] == 'OK' and not ProgrammingSubmits.objects.filter(username=submit['author']['members'][0]['handle'],
                                                                                        verdict='OK', task_id=submit['problem']['index'])):
                    print("New good Solve")
                    bonuses = 0
                    if not ProgrammingSubmits.objects.filter(task_id=submit['problem']['index'], verdict='OK'):
                        bonuses += (submit['problem']['index']) * 10
                    if not ProgrammingSubmits.objects.filter(programmingLanguage=submit['programmingLanguage'], verdict='OK',
                                                             username=submit['author']['members'][0]['handle']):
                        bonuses += 400
                    score = ProgScore.objects.filter(user=User.objects.filter(username=submit['author']['members'][0]['handle'])[0])
                    if (len(list(score)) == 0):
                        NewScoreObject = ProgScore(user=User.objects.filter(username=submit['author']['members'][0]['handle'])[0], score=self.ProgstdScore + bonuses + submit['problem']['index'] * 100,
                                                   pluser=self.ProgstdPlusser + submit['problem']['index'] * 2)
                        NewScoreObject.save()
                    else:
                        score[0].score += bonuses + submit['problem']['index'] * 100
                        score[0].pluser += submit['problem']['index'] * 2
                        score[0].save()
                submitObject.save()




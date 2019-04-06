"""
WSGI config for JudgeSystemSilaederOlymp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JudgeSystemSilaederOlymp.settings')

application = get_wsgi_application()

# Init ScoreView System

from results.scoreUpdate import ScoreUpdate
scoreViewer = ScoreUpdate(1000, 1000, 1000, 20, 20, 20, 'f6437fb3926edeb787fa410105f83746a6ede5d1', '65252f670708bf28d56d5a16a5c31c3579e2f6ec', 239990)
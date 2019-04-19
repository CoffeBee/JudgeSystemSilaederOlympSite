from .views import *
from django.urls import path

urlpatterns = [
    path('', math),
    path('shop/buy/<int:level>/', purchases),
    path('judge/', judge),
    path('judge/<int:submit_id>/', judge_task)
]

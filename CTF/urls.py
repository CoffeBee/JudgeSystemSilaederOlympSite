from .views import *
from django.urls import path

urlpatterns = [
    path('', ctf),
    path('shop/buy/<int:level>/', purchases),

]

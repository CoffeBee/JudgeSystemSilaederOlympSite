from .views import *
from django.urls import path

urlpatterns = [
    path('', programming),
    path('shop/buy/<int:level>/', purchases)
]

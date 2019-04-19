from django.urls import path
from .views import *

urlpatterns = [
    path('statement/<str:statement_hash>/', statement),
    path('setstd/', setstd),
    path('updateProg/', updateProg),
]

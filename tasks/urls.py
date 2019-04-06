from django.urls import path
from .views import *

urlpatterns = [
    path('/statement/<str:statement_hash>/', statement),

]

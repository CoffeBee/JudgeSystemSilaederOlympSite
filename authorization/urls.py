from .views import *
from django.urls import path

urlpatterns = [
    path('', login_view),
    path('logout/', logout_view),
]

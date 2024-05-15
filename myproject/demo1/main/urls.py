from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('registration', registration, name='registration'),
    path('login', auth, name='login'),
    path('loginAction', loginAction, name='loginAction'),
    path('orders', orders, name='orders'),
    path('makeorder', makeorder, name='makeorder'),
    path('logout', logout1, name='logout'),
    path('/makeorderAction', makeorderAction, name='makeorderAction'),
]

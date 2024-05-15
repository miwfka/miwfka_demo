
from datetime import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

def index(request):
    cars = Cars.objects.all()
    context = {'cars' : cars}
    return render(request, 'index.html', context)

def AppAction(request):
    if request.method == 'POST':
        car = request.POST['car']
        date = dt.strptime(request.POST['date'], '%Y-%m-%d')
        user = User.objects.get(id = request.user.id)
        mycar = Cars.objects.get(id = car)
        cardate = Application.objects.filter(date = date, car = car, status_id = 1)
        cardate2 = Application.objects.filter(date = date, car = car, status_id = 2)
        if cardate or cardate2:
            messages.error(request, 'НЕВЕРНО')
            return redirect('index')
        else:
            if date < dt.today():
                messages.error(request, 'НЕВЕРНО')
                return redirect('index')
            else:
                app = Application(user = user, date = date, car = mycar)
                app.save()

    return redirect('index')


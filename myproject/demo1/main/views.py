from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'login.html')

def orders(request):
    user = User.objects.get(id = request.user.id)
    orders = Orders.objects.filter(user_id = user)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

def makeorder(request):
    products = Products.objects.all().order_by('name')
    context = {'products': products}
    return render(request, 'makeorder.html', context)



def registration(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        mail = request.POST['mail']
        if User.objects.filter(username = login).exists():
            messages.error(request, 'Логин уже существует!')
            return redirect('main')
        else:
            if User.objects.filter(email = mail).exists():
                messages.error(request, 'Почта уже существует!')
                return redirect('main')
            else:
                user = User.objects.create_user(username=login, email=mail, password=password, first_name=name, last_name=phone)
                user.save()
                return redirect('login')
        


        


def loginAction(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin/')
            login(request, user)
            return redirect('orders')
        else:
            messages.error(request, 'НЕВЕРНО')
            return redirect('login')


def logout1(request):
    logout(request)
    return redirect('login')


def makeorderAction(request):
    if request.method == 'POST':
        name = request.POST['product']
        count = request.POST['count']
        address = request.POST['address']
        user = User.objects.get(id = request.user.id)
        product = Products.objects.get(id = name)
        status = Status.objects.get(id = 1)
        order = Orders(address=address, qty=count, user=user, products_id = product, status_id=status)
        order.save()

    return redirect('orders')
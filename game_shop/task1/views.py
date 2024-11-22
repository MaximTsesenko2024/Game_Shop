from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import Registation
from .models import *


# Create your views here.

def sign_up_by_django(request):
    def check_unic_name(users, username):
        for item in users:
            if item.name == username:
                return False
        return True
    info = {'title': 'Регистрация пользователя'}
    if request.method == 'POST':
        users = Buyer.objects.all()
        form = Registation(request.POST)
        if form.is_valid():
            if 'error' in info.keys():
                info.pop('error')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            balance = float(form.cleaned_data['balance'])
            if not check_unic_name(users, username):
                info['error'] = f'Пользователь {username} уже существует!'
            elif password != repeat_password:
                info['error'] = f'Пароли не совпадают!'
            else:
                Buyer.objects.create(name=username, age=age, balance=balance)
                return HttpResponse(f'Приветствуем, {username}!')
            form = Registation()
            info['form'] = form
            return render(request, 'registration_page.html', context=info)
    else:
        form = Registation()
        info['form'] = form
    return render(request, 'registration_page.html', context=info)


class MainWiew(TemplateView):
    template_name = 'main.html'
    extra_context = {'title': 'Главная страница'}


class SelGame(TemplateView):
    games = Game.objects.all()
    template_name = 'select_game.html'
    extra_context = {'title': 'Выбор игры', 'list_game': games}


class Car(TemplateView):
    template_name = 'car.html'
    car = []
    extra_context = {'title': 'Корзина'}

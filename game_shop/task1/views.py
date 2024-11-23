from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from .forms import Registation
from .models import *

count_page = 3


# Create your views here.

def sign_up_by_django(request: WSGIRequest):
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

def post_views(request: WSGIRequest):
    global count_page
    posts = Post.objects.all()
    count = request.GET.get('count')
    print(request.GET.get('count'))
    if count is None:
        count = count_page
    else:
        count_page = count
    paginator = Paginator(posts, count)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'post_views.html', {'page_obj': page_obj})


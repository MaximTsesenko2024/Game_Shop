from django import forms


class Registation(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(max_length=8, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    balance = forms.CharField(max_length=5, label='Введите свой баланс')
    age = forms.CharField(max_length=3, label='Введите свой возраст')

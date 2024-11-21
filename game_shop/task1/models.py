from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=8, max_digits=8)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=8, max_digits=8)
    size = models.DecimalField(decimal_places=8, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(db_default=False)
    buyer = models.ManyToManyField(to="Buyer", related_name="games")


"""
Game - модель представляющая игру.

Обладает следующими полями:

title - название игры

cost - цена(DecimalField)

size - размер файлов игры(DecimalField)

description - описание(неограниченное кол-во текста)

age_limited - ограничение возраста 18+ (BooleanField, по умолчанию False)

buyer - покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.

DecimalField - поле для дробных чисел.

BooleanField - поле для булевых значений.
"""

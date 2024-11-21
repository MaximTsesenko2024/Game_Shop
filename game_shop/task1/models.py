from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=8)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    size = models.DecimalField(decimal_places=0, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(db_default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title


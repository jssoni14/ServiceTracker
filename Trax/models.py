from django.db import models
import datetime


class User(models.Model):
    name = models.CharField(max_length=75, null=True)


class Car(models.Model):

    make = models.CharField(max_length=35)
    model = models.CharField(max_length=75)
    year = models.IntegerField()
    mileage = models.IntegerField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)


class Service(models.Model):
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    service = models.CharField(max_length=150)
    mileage = models.IntegerField()
    car = models.CharField(max_length=75)



# Create your models here.

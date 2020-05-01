from django.db import models


# Create your models here.
class Car(models.Model):
    license_plate = models.CharField(max_length=6)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)


class Owner(models.Model):
    SEX_CHOISES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'Unspecified')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOISES)
    cars = models.ManyToManyField(Car, through='Ownership')


class DriverLicense(models.Model):
    TYPE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    ]
    number = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
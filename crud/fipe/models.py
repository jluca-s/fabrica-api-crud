from django.db import models

class Vehicle(models.Model):
    price = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    modelYear = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    codeFipe = models.CharField(max_length=50, unique=True, primary_key=True)
    vehicleType = models.CharField(max_length=50)
    fuelType = models.CharField(max_length=50)
    
    def __str__(self):
        return self.model
from django.db import models

# Create your models here.

class Plane(models.Model):
    name = models.CharField(max_length=15)
    seats_first_class = models.IntegerField()
    seats_business = models.IntegerField()
    seats_economy = models.IntegerField()
    luggage_capacity = models.FloatField() # kg
    
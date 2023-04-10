from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Plane(models.Model):
    name = models.CharField(max_length=15)
    seats_first_class = models.IntegerField(validators=[MinValueValidator(1)])
    seats_business = models.IntegerField(validators=[MinValueValidator(1)])
    seats_economy = models.IntegerField(validators=[MinValueValidator(1)])
    luggage_capacity = models.FloatField(validators=[MinValueValidator(0.0)]) # kg
    
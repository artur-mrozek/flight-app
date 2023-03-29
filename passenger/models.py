from django.db import models

# Create your models here.

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport_number = models.CharField(max_length=8)
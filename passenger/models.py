from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    passport_number = models.CharField(max_length=8)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
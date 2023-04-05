from django.db import models
from plane.models import Plane

# Create your models here.

class Flight(models.Model):
    start_place = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    price_first_class = models.FloatField()
    price_business_class = models.FloatField()
    price_economy_class = models.FloatField()
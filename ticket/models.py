from django.db import models
from passenger.models import Passenger
from flight.models import Flight


# Create your models here.

class Ticket(models.Model):
    CLASS_CHOICES = (
    ("first","first"),
    ("business","business"),
    ("economy","economy")
    )   
    
    seat_number = models.IntegerField()
    seat_class = models.CharField(max_length=10, choices=CLASS_CHOICES, default="economy")
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
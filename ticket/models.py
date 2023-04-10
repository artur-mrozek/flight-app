from django.db import models
from passenger.models import Passenger
from flight.models import Flight
from django.core.validators import MinValueValidator


# Create your models here.

class Ticket(models.Model):
    CLASS_CHOICES = (
    ("First","First"),
    ("Business","Business"),
    ("Economy","Economy")
    )   
    
    seat_number = models.IntegerField(validators=[MinValueValidator(1)])
    seat_class = models.CharField(max_length=10, choices=CLASS_CHOICES, default="economy")
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
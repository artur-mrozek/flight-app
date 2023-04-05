from django import forms
from flight.models import Flight
from django.core.exceptions import ValidationError
from .models import Ticket

class BuyTicketForm(forms.Form):
    CLASS_CHOICES = (
    ("first","first"),
    ("business","business"),
    ("economy","economy")
    )

    def __init__(self, *args, **kwargs):
        self.flight_id = kwargs.pop("flight_id")
        super(BuyTicketForm, self).__init__(*args, **kwargs)
    
    seat_number = forms.IntegerField(label='Seat number')
    seat_class = forms.ChoiceField(label='Class', choices=CLASS_CHOICES)
    luggage = forms.FloatField(label="Luggage")

    def clean_seat_number(self):
        data = self.cleaned_data["seat_number"]
        flight = Flight.objects.get(id=self.flight_id)
        seats_total = flight.plane_id.seats_first_class + flight.plane_id.seats_business + flight.plane_id.seats_economy
        tickets = Ticket.objects.filter(flight_id=flight)
        occupied_seats = []
        for ticket in tickets:
            occupied_seats.append(ticket.seat_number)
        if data <= 0 or data > seats_total:
            raise ValidationError("Wybierz odpowiedni nr miejsca")
        if data in occupied_seats:
            raise ValidationError("To miejsce jest już zajęte")
        
    def clean_luggage(self):
        data = float(self.cleaned_data["luggage"])
        flight = Flight.objects.get(id=self.flight_id)
        if data > flight.plane_id.luggage_capacity:
            raise ValidationError("Twój bagaż jest za ciężki")
        if data < 0:
            raise ValidationError("Podaj odpowiednią wagę bagażu")
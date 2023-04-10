from django.shortcuts import render, redirect
from .forms import BuyTicketForm
from django.shortcuts import get_object_or_404
from flight.models import Flight
from .models import Ticket
from passenger.models import Passenger

# Create your views here.

def buy_ticket_view(request, *args, **kwargs):
    flight_id = request.GET.get('flight','')
    flight = get_object_or_404(Flight, pk=flight_id)
    passenger = Passenger.objects.get(user_id=request.user)
    form = BuyTicketForm(flight_id=flight_id)
    price_first_class = flight.price_first_class
    price_business_class = flight.price_business_class
    price_economy_class = flight.price_economy_class
    seats_total = flight.plane_id.seats_first_class + flight.plane_id.seats_business + flight.plane_id.seats_economy
    seats_first_class = flight.plane_id.seats_first_class
    seats_business = flight.plane_id.seats_business
    seats_economy = flight.plane_id.seats_economy
    luggage = flight.plane_id.luggage_capacity
    tickets = Ticket.objects.filter(flight_id=flight)

    if request.method == 'POST':
        form = BuyTicketForm(request.POST, flight_id=flight_id)
        if form.is_valid():
            ticket = Ticket(seat_number=request.POST['seat_number'],seat_class=request.POST['seat_class'],passenger_id=passenger,flight_id=flight)
            ticket.save()
            if request.POST['seat_class'] == "First":
                flight.plane_id.seats_first_class = flight.plane_id.seats_first_class - 1
            if request.POST['seat_class'] == "Business":
                flight.plane_id.seats_business = flight.plane_id.seats_business - 1
            if request.POST['seat_class'] == "Economy":
                flight.plane_id.seats_economy = flight.plane_id.seats_economy - 1
            flight.plane_id.luggage_capacity = flight.plane_id.luggage_capacity - float(request.POST['luggage'])
            flight.plane_id.save()
            return redirect('/')
    context = {
        "form": form,
        "price_first_class": price_first_class,
        "price_business_class": price_business_class,
        "price_economy_class": price_economy_class,
        "seats_total": seats_total,
        "tickets": tickets,
        "seats_first_class": seats_first_class,
        "seats_business": seats_business,
        "seats_economy": seats_economy,
        "luggage": luggage
        }
    return render(request, "ticket/buy_ticket.html", context)

def my_tickets_view(request, *args, **kwargs):
    passenger = Passenger.objects.get(user_id=request.user)
    tickets = Ticket.objects.filter(passenger_id=passenger)
    context = {"tickets": tickets}
    return render(request, "ticket/my_tickets.html", context)
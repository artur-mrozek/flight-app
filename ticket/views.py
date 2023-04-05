from django.shortcuts import render, redirect
from .forms import BuyTicketForm
from django.shortcuts import get_object_or_404
from flight.models import Flight
from .models import Ticket
from passenger.models import Passenger

# Create your views here.

def buy_ticket_view(request, *args, **kwargs):
    flight = get_object_or_404(Flight, pk=request.GET.get('flight',''))
    passenger = Passenger.objects.get(user_id=request.user)
    print(passenger)
    form = BuyTicketForm()
    price_first_class = flight.price_first_class
    price_business_class = flight.price_business_class
    price_economy_class = flight.price_economy_class

    if request.method == 'POST':
        form = BuyTicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket(seat_number=request.POST['seat_number'],seat_class=request.POST['seat_class'],passenger_id=passenger,flight_id=flight)
            ticket.save()
            return redirect('/')
    context = {
        "form": form,
        "price_first_class": price_first_class,
        "price_business_class": price_business_class,
        "price_economy_class": price_economy_class
        }
    return render(request, "ticket/buy_ticket.html", context)
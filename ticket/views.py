from django.shortcuts import render

# Create your views here.

def buy_ticket_view(request, *args, **kwargs):
    context = {}
    return render(request, "ticket/buy_ticket.html", context)
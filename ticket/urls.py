
from django.urls import path

from .views import buy_ticket_view, my_tickets_view

app_name = "ticket"
urlpatterns = [
    path('buy/', buy_ticket_view, name="buy_ticket"),
    path('my-tickets/', my_tickets_view, name="buy_ticket"),
]
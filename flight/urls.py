
from django.urls import path

from .views import flights_list_view

app_name = "flight"
urlpatterns = [
    path('', flights_list_view, name="flights_list"),
]
from django.shortcuts import render, redirect

from .models import Flight

# Create your views here.

def flights_list_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/passenger/login")
    queryset = Flight.objects.all()
    context = {"queryset": queryset}
    return render(request, "flight/flights_list.html", context)
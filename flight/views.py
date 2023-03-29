from django.shortcuts import render, redirect


# Create your views here.

def flights_list_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/passenger/login")
    context = {}
    return render(request, "flight/flights_list.html")
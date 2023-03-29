from django.shortcuts import render

# Create your views here.

def flights_list_view(request, *args, **kwargs):
    context = {}
    return render(request, "flight/flights_list.html")
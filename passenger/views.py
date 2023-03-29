from django.shortcuts import render

# Create your views here.
def login_view(request, *args, **kwargs):
    context = {}
    return render(request, "passenger/login.html", context)

def register_view(request, *args, **kwargs):
    context = {}
    return render(request, "passenger/register.html", context)
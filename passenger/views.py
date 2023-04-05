from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

from .models import Passenger

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/passenger/login/')
    context = {"form": form}
    return render(request, "passenger/login.html", context)

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
            user.save()
            passenger = Passenger(first_name=request.POST['first_name'],last_name=request.POST['last_name'],passport_number=request.POST['passport_number'],user_id=user)
            passenger.save()
            login(request, user)
            return redirect('/')

    context = {"form": form}
    return render(request, "passenger/register.html", context)
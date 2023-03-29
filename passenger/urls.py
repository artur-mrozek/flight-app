
from django.urls import path

from .views import login_view, register_view

app_name = "passenger"
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
]
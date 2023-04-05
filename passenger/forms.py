from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=25, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    email = forms.EmailField(label="Email", max_length=25)
    password = forms.CharField(label='Password', max_length=25, widget=forms.PasswordInput())
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    passport_number = forms.CharField(label='Passport number', max_length=8)
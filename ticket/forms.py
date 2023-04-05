from django import forms

class BuyTicketForm(forms.Form):
    CLASS_CHOICES = (
    ("first","first"),
    ("business","business"),
    ("economy","economy")
    )  
    
    seat_number = forms.IntegerField(label='Seat number')
    seat_class = forms.ChoiceField(label='Class', choices=CLASS_CHOICES)
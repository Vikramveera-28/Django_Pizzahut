from django import forms
from .models import Pizza

class OrderForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            'name',
            'phone',
            'email',
            'item',
            'size'
        ]
        labels = {
            'name': "Name",
            'phone': "Phone",
            'email': "Email",
            'item': "Item",
            'size': "Size"
        }

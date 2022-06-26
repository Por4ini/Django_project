from django.forms import ModelForm
from .models import Contacts, Request
from django import forms


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'role', 'phone', 'messenger')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'messenger': forms.TextInput(attrs={'class': 'form-control'}),

        }

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['email', 'hromada']

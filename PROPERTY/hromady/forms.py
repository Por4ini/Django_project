from django import forms
from django.forms import ModelForm
from .models import CommunityHromady, Advertisement


class EmblemForm(ModelForm):
    class Meta:
        model = CommunityHromady
        fields = ['flag', 'emblem']
        widgets = {
            'flag': forms.FileInput(attrs={'class': 'form-control'}),
            'emblem': forms.FileInput(attrs={'class': 'form-control'}),
        }
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title_advertisement', 'advertisement', "image_advertisement"]
        widgets = {
            'title_advertisement': forms.TextInput(attrs={'class': 'form-control'}),
            'advertisement': forms.Textarea(attrs={'class': 'form-control'}),
            'image_advertisement': forms.FileInput(attrs={'class': 'form-control'}),
        }
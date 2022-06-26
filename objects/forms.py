from django.forms import ModelForm
from .models import Object, ObjectImages, ObjectDocuments
from django import forms


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ('title', 'address', 'components', 'share_size', 'total_area', 'extra')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'components': forms.TextInput(attrs={'class': 'form-control'}),
            'share_size': forms.TextInput(attrs={'class': 'form-control'}),
            "total_area": forms.TextInput(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "documents": forms.FileInput(attrs={'class': 'form-control'}),
            'extra': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ObjectsImageForm(ModelForm):
    class Meta:
        model = ObjectImages
        fields = ["title", 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ObjectsDocumentsForm(ModelForm):
    class Meta:
        model = ObjectDocuments
        fields = ["title", 'documents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'documents': forms.FileInput(attrs={'class': 'form-control'}),
        }

from django.forms import ModelForm
from .models import Subjects, SubjectImages, SubjectDocuments
from django import forms


class SubjectsForm(ModelForm):
    class Meta:
        model = Subjects
        fields = ["title", "balance_holder", "status", "components", "part_size", "area", "period_of_use",  'extra']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'balance_holder': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'components': forms.TextInput(attrs={'class': 'form-control'}),
            'part_size': forms.TextInput(attrs={'class': 'form-control'}),
            "area": forms.TextInput(attrs={'class': 'form-control'}),
            "period_of_use": forms.TextInput(attrs={'class': 'form-control'}),
            'extra': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SubjectsImageForm(ModelForm):
    class Meta:
        model = SubjectImages
        fields = ["title", 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SubjectsDocumentsForm(ModelForm):
    class Meta:
        model = SubjectDocuments
        fields = ["title", 'documents']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'documents': forms.FileInput(attrs={'class': 'form-control'}),
        }

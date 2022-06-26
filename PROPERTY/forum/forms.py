from django.forms import ModelForm
from .models import Post, Topic
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms
from django.forms.models import ModelForm
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm, ModelForm):
    email = forms.EmailField(label='Введіть вашу пошту', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(label='Та й підтвердіть капчу')

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')



class CustomUserChangeForm(UserChangeForm):
    username = forms.EmailField(label='Введіть вашу пошту', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Введіть вашу пошту', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(label="Та й підтвердіть капчу")

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'photo', 'extra']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            "photo": forms.FileInput(attrs={'class': 'form-control'}),
            'extra': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ChangeCommunityForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['community']
        widgets = {
            'community': forms.TextInput(attrs={'class': 'form-control'})
        }


class ChangeRoleForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'})
        }
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms
from django.forms.models import ModelForm
from captcha.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm, ModelForm):
    email = forms.EmailField(label='Введіть вашу пошту')
    password1 = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput)
    captcha = ReCaptchaField(label='Та й підтвердіть капчу')


    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'community')


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = ('email',)


class UserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(label="Та й підтвердіть капчу")

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    widgets = {
        'email': forms.EmailInput(attrs={"class": "form-floating mb-3"}),
        'password': forms.PasswordInput(attrs={"class": "form-floating mb-3"}),


    }

from .models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages

def home(request):
    title = 'Головна сторінка'
    return render(request, 'user/home.html', {'title': title})

def profile_view(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    title = 'Особистий кабінет'
    return render(request, 'user/profile_view.html', {'profile': profile, 'title': title})


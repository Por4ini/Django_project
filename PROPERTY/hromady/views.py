from django.shortcuts import render
from .models import CommunityHromady
from user.models import CustomUser

def home(request):
    community = CommunityHromady.objects.all()
    user_info = CustomUser.objects.all()
    title = 'Головна сторінка'
    context = {'title': title,
               'community': community,
               'user_info': user_info}
    return render(request, 'hromady/home.html', {'context': context})


def community(requrst):
    user_naw = CustomUser.objects.all()
    hromada = CommunityHromady.objects.filter(pk=user_naw)
    title = 'Громада'
    return render(requrst, 'hromady/hromady.html', {'hromada': hromada, 'title': title, 'user_naw': user_naw})

def search(request):
    hromady = CommunityHromady.objects.filter(district__icontains=request.GET.get('s'))
    return render(request, 'hromady/search.html', {'hromady': hromady})

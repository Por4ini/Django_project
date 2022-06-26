from django.http import JsonResponse
from django.shortcuts import render
from user.models import CustomUser
from .models import CommunityHromady, Advertisement
from objects.models import Object
from administrator.models import Contacts
import json


def home(request):
    hromady = CommunityHromady.objects.all()

    return render(request, 'hromady/home.html', {'hromady': hromady})


def hromada(request, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    objects = Object.objects.filter(hromada_id=hromada_id)
    advertisement = Advertisement.objects.filter(community_id=hromada_id)
    contacts = Contacts.objects.filter(hromada_id=hromada_id)
    return render(request, 'hromady/hromada_page.html', {'hromada': hromada, 'objects': objects,
                                                         'advertisement': advertisement, 'contacts': contacts})


def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = CommunityHromady.objects.filter(locality__icontains=query_original)
    for item in queryset:
        locality = item.locality
        type = item.type
        district = item.district
        region = item.region

    mylist = []
    mylist += [x.locality for x in queryset], f'{locality} {type} {district} {region}'

    return JsonResponse(mylist, safe=False)


def community(request):
    print(request.GET)
    hromada = CommunityHromady.objects.filter(locality__icontains=request.GET.get("q")[0:3])
    title = 'Громада'
    return render(request, 'hromady/hromady.html', {'hromada': hromada, 'title': title})


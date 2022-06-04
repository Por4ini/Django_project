from django.shortcuts import render
from .models import Object

def get_objects(request):
    objects = Object.objects.all()
    title = "Об'экти"
    return render(request, 'objects/objects.html', {'objects': objects, 'title':title})
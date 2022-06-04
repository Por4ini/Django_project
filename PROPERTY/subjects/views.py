from django.shortcuts import render
from .models import Subjects


def get_subjects(request):
    subjects = Subjects.objects.all()
    title = "Суб'екти"
    return render(request, 'objects/subjects/subjects.html', {'subjects':subjects, 'title':title})
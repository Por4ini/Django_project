from django.shortcuts import render, redirect

from user.decorators import subject_manager
from .models import Subjects, SubjectDocuments, SubjectImages
from .forms import SubjectsForm, SubjectsDocumentsForm, SubjectsImageForm
from objects.models import Object


def get_subjects(request, pk, code):
    subjects = Subjects.objects.filter(id=pk)
    for item in subjects:
        data = item.id
    image = SubjectImages.objects.filter(subject_id=data)
    documents = SubjectDocuments.objects.filter(subject_id=data)
    title = "Суб'ект "
    return render(request, 'objects/subjects/subjects.html',
                  {'code': code, 'subjects': subjects, 'title': title, 'image': image, 'documents': documents})


@subject_manager
def create_subject(request, pk, code):
    form = SubjectsForm()
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.object_id = pk
            subject.save()
            link = f'/{code}/object/{pk}'
            return redirect(link)
    return render(request, 'objects/subjects/create_subject.html', {'form': form})


@subject_manager
def update_subject(request, pk, code):
    subjects = Subjects.objects.get(id=pk)
    a = Subjects.objects.filter(id=pk)
    for item in a:
        objects_id = item.object_id
    form = SubjectsForm(instance=subjects)
    if request.method == 'POST':
        form = SubjectsForm(request.POST, instance=subjects)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.object_id = objects_id
            subject.save()
            link = f'/{code}/object/{objects_id}'
            return redirect(link)
    return render(request, 'objects/subjects/create_subject.html', {'form': form})


@subject_manager
def delete_subject(request, pk, code):
    subject = Subjects.objects.get(id=pk)
    object_id = subject.object_id

    if request.method == "POST":
        subject.delete()
        link = f'/{code}/object/{object_id}'
        return redirect(link)
    return render(request, 'objects/subjects/delete_subject.html', {'item': subject})


@subject_manager
def create_subject_image(request, code, pk):
    form = SubjectsImageForm()
    if request.method == 'POST':
        form = SubjectsImageForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.subject_id = pk
            subject.save()
            link = f'/{code}/object/subject/{pk}'
            return redirect(link)

    return render(request, 'objects/subjects/create_subject.html', {'form': form, 'code': code, 'pk': pk})


@subject_manager
def delete_subject_image(request, code, pk):
    data = SubjectImages.objects.get(pk=pk)
    num = data.subject_id
    if request.method == "POST":
        data.delete()
        link = f"/{code}/object/subject/{num}"
        return redirect(link)
    return render(request, 'objects/subjects/delete_image.html', {'data': data, 'code': code, 'pk': pk})


@subject_manager
def create_subject_document(request, code, pk):
    form = SubjectsDocumentsForm()
    if request.method == 'POST':
        form = SubjectsDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.subject_id = pk
            subject.save()
            link = f'/{code}/object/subject/{pk}'
            return redirect(link)

    return render(request, 'objects/subjects/create_subject.html', {'form': form, 'code': code, 'pk': pk})


@subject_manager
def delete_subject_document(request, code, pk):
    data = SubjectDocuments.objects.get(pk=pk)
    num = data.subject_id
    if request.method == "POST":
        data.delete()
        link = f"/{code}/object/subject/{num}"
        return redirect(link)
    return render(request, 'objects/subjects/delete_document.html', {'data': data, 'code': code, 'pk': pk})

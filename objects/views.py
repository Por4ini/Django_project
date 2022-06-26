from django.shortcuts import render, redirect
from .models import Object, ObjectImages, ObjectDocuments
from subjects.models import Subjects
from .forms import ObjectForm, ObjectsImageForm, ObjectsDocumentsForm
from hromady.models import CommunityHromady
from user.decorators import object_manager


def get_objects(request, id, code):
    objects = Object.objects.filter(pk=id)
    subjects = Subjects.objects.filter(object_id=id)
    title = "Об'єкт"
    image = ObjectImages.objects.filter(object_id=id)
    documents = ObjectDocuments.objects.filter(object_id=id)
    return render(request, 'objects/objects.html',
                  {'objects': objects, 'title': title, 'subjects': subjects, "code": code, 'image': image,
                   'documents': documents, })


@object_manager
def create_object(request, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    form = ObjectForm()
    if request.method == 'POST':
        form = ObjectForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.hromada_id = hromada_id
            print(object)
            object.save()
            link = f"/{code}"
            return redirect(link)
    return render(request, 'objects/create_object.html', {'form': form, 'code': code})


@object_manager
def update_object(request, pk, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    object = Object.objects.get(id=pk)
    form = ObjectForm(instance=object)
    if request.method == 'POST':
        form = ObjectForm(request.POST, instance=object)
        if form.is_valid():
            object = form.save(commit=False)
            object.hromada_id = hromada_id
            object.save()
            link = f"/{code}"
            return redirect(link)
    return render(request, 'objects/create_object.html', {'form': form, 'code': code})


@object_manager
def delete_object(request, pk, code):
    data = Object.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        link = f"/{code}"
        return redirect(link)
    return render(request, 'objects/delete_object.html', {'data': data, 'code': code})


@object_manager
def create_object_image(request, code, pk):
    form = ObjectsImageForm()
    if request.method == 'POST':
        form = ObjectsImageForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.object_id = pk
            object.save()
            link = f"/{code}/object/{pk}"
            return redirect(link)
    return render(request, 'objects/create_object.html', {'form': form, 'code': code, 'pk': pk})


@object_manager
def delete_object_image(request, code, pk):
    data = ObjectImages.objects.get(pk=pk)
    num = data.object_id
    if request.method == "POST":
        data.delete()
        link = f"/{code}/object/{num}"
        return redirect(link)
    return render(request, 'objects/delete_image.html', {'data': data, 'code': code, 'pk': pk})


@object_manager
def create_object_document(request, code, pk):
    form = ObjectsDocumentsForm()
    if request.method == 'POST':
        form = ObjectsDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.object_id = pk
            document.save()
            link = f"/{code}/object/{pk}"
            return redirect(link)
    return render(request, 'objects/create_object.html', {'form': form, 'code': code, 'pk': pk})


@object_manager
def delete_object_document(request, code, pk):
    data = ObjectDocuments.objects.get(pk=pk)
    num = data.object_id
    if request.method == "POST":
        data.delete()
        link = f"/{code}/object/{num}"
        return redirect(link)
    return render(request, 'objects/delete_document.html', {'data': data, 'code': code, 'pk': pk})

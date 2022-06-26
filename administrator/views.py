from django.shortcuts import render, redirect
from user.forms import CustomUserForm, ChangeRoleForm
from user.models import CustomUser
from hromady.models import CommunityHromady, Advertisement
from objects.models import Object, ObjectImages, ObjectDocuments
from subjects.models import Subjects, SubjectDocuments, SubjectImages
from objects.forms import ObjectForm, ObjectsImageForm, ObjectsDocumentsForm
from subjects.forms import SubjectsForm, SubjectsImageForm, SubjectsDocumentsForm
from .models import Contacts, Request
from .forms import ContactsForm
from hromady.forms import EmblemForm, AdvertisementForm
from user.decorators import admin_only


@admin_only
def hromada_admin(request, code):
    hromada = CommunityHromady.objects.get(code=code)
    objects = Object.objects.filter(hromada_id=hromada.id)
    if request.method == 'POST':
        hromada.registration = 1
        print(hromada)
        hromada.save()
        return redirect(f'/{code}/administrator/')

    return render(request, 'hromady/admin/hromada_admin.html', {'hromada': hromada, 'objects': objects})


@admin_only
def user_admin(request, code):
    com = CommunityHromady.objects.get(code=code)
    users = CustomUser.objects.filter(community_id=com.id)

    return render(request, 'hromady/admin/users.html', {'users': users})


@admin_only
def update_user_admin(request, pk, code):
    user = CustomUser.objects.get(id=pk)
    form = CustomUserForm(instance=user)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            link = f"/{code}/administrator/users/"
            return redirect(link)
    title = 'Редагувати профіль'

    return render(request, 'hromady/admin/update_user.html', {"form": form,
                                                              "user": user,
                                                              "title": title,
                                                              'code': code})


@admin_only
def delete_user_admin(request, code):
    pass


@admin_only
def objects_admin(request, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    objects = Object.objects.filter(hromada_id=hromada_id)
    title = "Об'єкти"

    return render(request, 'hromady/admin/objects.html',
                  {'code': code, 'objects': objects, 'hromada': hromada, 'title': title})


@admin_only
def create_object_admin(request, code):
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
            link = f"/{code}/administrator/objects/"
            return redirect(link)
    return render(request, 'hromady/admin/create_object.html', {'form': form, 'code': code})


@admin_only
def update_object_admin(request, pk, code):
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
            link = f"/{code}/administrator/objects/"
            return redirect(link)
    return render(request, 'hromady/admin/create_object.html', {'form': form, 'code': code})


@admin_only
def delete_object_admin(request, pk, code):
    data = Object.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        link = f"/{code}/administrator/objects/"
        return redirect(link)
    return render(request, 'hromady/admin/delete_object.html', {'data': data, 'code': code})


@admin_only
def subjects_admin(request, pk, code):
    objects = Object.objects.filter(id=pk)
    for item in objects:
        data = item.id
    subjects = Subjects.objects.filter(object_id=data)
    title = "Суб'єкт"

    return render(request, 'hromady/admin/subjects.html',
                  {'subjects': subjects, 'objects': objects, 'title': title, "code": code})


@admin_only
def create_subject_admin(request, pk, code):
    form = SubjectsForm()
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.object_id = pk
            subject.save()
            link = f'/{code}/administrator/object/subjects/{pk}'
            return redirect(link)
    return render(request, 'hromady/admin/create_subject.html', {'form': form})


@admin_only
def update_subject_admin(request, pk, code):
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
            link = f'/{code}/administrator/object/subjects/{objects_id}'
            return redirect(link)
    return render(request, 'hromady/admin/create_subject.html', {'form': form})


@admin_only
def delete_subject_admin(request, pk, code):
    subject = Subjects.objects.get(id=pk)
    object_id = subject.object_id

    if request.method == "POST":
        subject.delete()
        link = f'/{code}/administrator/object/subjects/{object_id}'
        return redirect(link)
    return render(request, 'hromady/admin/delete_subject.html', {'item': subject})


@admin_only
def contact_admin(request, code):
    com = CommunityHromady.objects.filter(code=code)
    for item in com:
        com_id = item.id
    contacts = Contacts.objects.filter(hromada_id=com_id)
    return render(request, 'hromady/admin/contacts.html', {'contacts': contacts, 'com': com})


@admin_only
def create_contact_admin(request, pk, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    form = ContactsForm()
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.hromada_id = hromada_id
            contact.save()
            link = f'/{code}/administrator/contacts'
            return redirect(link)
    return render(request, 'hromady/admin/create_subject.html', {'form': form})


@admin_only
def update_contact_admin(request, code, pk):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    contact = Contacts.objects.get(id=pk)
    form = ContactsForm(instance=contact)

    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.object_id = hromada_id
            contact.save()
            link = f'/{code}/administrator/contacts'
            return redirect(link)
    return render(request, 'hromady/admin/create_subject.html', {'form': form})


@admin_only
def delete_contact_admin(request, pk, code):
    data = Contacts.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        link = f"/{code}/administrator/contacts/"
        return redirect(link)
    return render(request, 'hromady/admin/delete_contact.html', {'data': data, 'code': code})


@admin_only
def update_image(request, code):
    form = EmblemForm()
    data = CommunityHromady.objects.get(code=code)
    if request.method == 'POST':
        form = EmblemForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.code = code
            data.save()
        link = f'/{code}/administrator'
        return redirect(link)

    return render(request, 'hromady/admin/update_emblem.html', {'form': form})


@admin_only
def advertisement(request, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    advertisement = Advertisement.objects.filter(community_id=hromada_id)

    return render(request, 'hromady/admin/advertisement.html', {'data': advertisement, 'com': hromada})


@admin_only
def create_advertisement(request, code):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    form = AdvertisementForm()
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.community_id = hromada_id
            advertisement.save()
            link = f"/{code}/administrator/advertisement"
            return redirect(link)
    return render(request, 'hromady/admin/create_advertisement.html', {'form': form, 'code': code})


@admin_only
def update_advertisement(request, code, pk):
    hromada = CommunityHromady.objects.filter(code=code)
    for item in hromada:
        hromada_id = item.id
    advertisement = Advertisement.objects.get(id=pk)
    form = AdvertisementForm(instance=advertisement)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.community_id = hromada_id
            advertisement.save()
            link = f"/{code}/administrator/advertisement"
            return redirect(link)
    return render(request, 'hromady/admin/create_advertisement.html', {'form': form, 'code': code})


@admin_only
def delete_advertisement(request, pk, code):
    data = Advertisement.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        link = f"/{code}/administrator/advertisement"
        return redirect(link)
    return render(request, 'hromady/admin/delete_advertisement.html', {'data': data, 'code': code})


def subject_image(request, pk, code):
    image = SubjectImages.objects.filter(subject_id=pk)

    return render(request, 'hromady/admin/item/image.html', {'image': image, 'code': code, 'pk': pk, 'image': image})


def create_subject_image(request, code, pk):
    form = SubjectsImageForm()
    if request.method == 'POST':
        form = SubjectsImageForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.subject_id = pk
            subject.save()
            return redirect(f'/{code}/administrator/object/subjects/image/{pk}')

    return render(request, 'hromady/admin/item/create.html', {'form': form, 'code': code, 'pk': pk})


def delete_subject_image(request, code, pk):
    image = SubjectImages.objects.get(pk=pk)
    num = image.subject_id
    if request.method == "POST":
        image.delete()
        return redirect(f'/{code}/administrator/object/subjects/image/{num}')
    return render(request, 'hromady/admin/item/delete.html', {'code': code, 'pk': pk, 'num':num})


def subject_document(request, pk, code):
    document = SubjectDocuments.objects.filter(subject_id=pk)

    return render(request, 'hromady/admin/item/document.html', {'document': document, 'code': code, 'pk': pk})


def create_subject_document(request, pk, code):
    form = SubjectsDocumentsForm()
    if request.method == 'POST':
        form = SubjectsDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.subject_id = pk
            subject.save()
            return redirect(f'/{code}/administrator/object/subjects/document/{pk}')

    return render(request, 'hromady/admin/item/create.html', {'form': form, 'code': code, 'pk': pk})


def delete_subject_document(request, pk, code):
    document = SubjectDocuments.objects.get(pk=pk)
    num = document.subject_id
    if request.method == "POST":
        document.delete()
        return redirect(f'/{code}/administrator/object/subjects/document/{num}')
    return render(request, 'hromady/admin/item/delete_doc.html', {'code': code, 'pk': pk, 'num': num})


# !
def object_image(request, pk, code):
    image = ObjectImages.objects.filter(object_id=pk)

    return render(request, 'hromady/admin/item/image.html', {'image': image, 'code': code, 'pk': pk})


def create_object_image(request, pk, code):
    form = ObjectsImageForm()
    if request.method == 'POST':
        form = ObjectsImageForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.subject_id = pk
            object.save()
            return redirect(f'/{code}/administrator/object/image/{pk}')

    return render(request, 'hromady/admin/item/create.html', {'form': form, 'code': code, 'pk': pk})


def delete_object_image(request, pk, code):
    image = ObjectImages.objects.get(pk=pk)
    num = image.object_id
    if request.method == "POST":
        image.delete()
        return redirect(f'/{code}/administrator/object/document/{num}')
    return render(request, 'hromady/admin/item/delete_obj_img.html', {'code': code, 'pk': pk, 'num': num})


# !
def object_document(request, pk, code):
    document = ObjectDocuments.objects.filter(object_id=pk)

    return render(request, 'hromady/admin/item/doc_obj.html', {'document': document, 'code': code, 'pk': pk})


def create_object_document(request, pk, code):
    form = ObjectsDocumentsForm()
    if request.method == 'POST':
        form = ObjectsDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.object_id = pk
            object.save()
            return redirect(f'/{code}/administrator/object/document/{pk}')

    return render(request, 'hromady/admin/item/create.html', {'form': form, 'code': code, 'pk': pk})


def delete_object_document(request, pk, code):
    document = ObjectDocuments.objects.get(pk=pk)
    num = document.object_id
    if request.method == "POST":
        document.delete()
        return redirect(f'/{code}/administrator/object/document/{num}')
    return render(request, 'hromady/admin/item/delete_obj_doc.html', {'code': code, 'pk': pk, 'num': num})

# !

def request(request):
    data = Request.objects.all()

    return render(request, 'hromady/admin/request/requests_page.html', {'data': data})


def request_success(request, pk):
    data = Request.objects.get(id=pk)

    user_data = CustomUser.objects.get(email=data.email)
    if request.method == "POST":
        user_data.role_id = 2
        user_data.save()
        data.delete()
        return redirect('requests')
    return render(request, 'hromady/admin/request/access.html', {'data': data, 'user_data': user_data})


def request_denial(request, pk):
    data = Request.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('requests')
    return render(request, 'hromady/admin/request/denial.html', {'data': data})


def change_roll(request, pk, code):
    data = CustomUser.objects.get(pk=pk)

    form = ChangeRoleForm(instance=data)

    if request.method == 'POST':
        form = ChangeRoleForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.id = pk
            user_data.save()
            return redirect(f'/{code}/administrator/users/')
    return render(request, 'hromady/admin/change_role.html', {'form': form, 'code': code})


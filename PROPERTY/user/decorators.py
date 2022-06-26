from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('hromady:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.role.title == 'Адміністратор громади':
            print('Совпало')
            return view_func(request, *args, **kwargs)

        else:
            print('не совпало')
            return redirect('hromady:home')

    return wrapper_func


def object_manager(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.role.title == 'Технік':
            print('Совпало')
            return view_func(request, *args, **kwargs)
        elif request.user.role.title == 'Адміністратор громади':
            print('Совпало')
            return view_func(request, *args, **kwargs)

        else:
            print('не совпало')
            return redirect('hromady:home')

    return wrapper_func


def subject_manager(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.role.title == 'Технік':
            print('Совпало')
            return view_func(request, *args, **kwargs)
        elif request.user.role.title == 'Адміністратор громади':
            print('Совпало')
            return view_func(request, *args, **kwargs)
        elif request.user.role.title == 'Бухгалтер':
            print('Совпало')
            return view_func(request, *args, **kwargs)


        else:
            print('не совпало')
            return redirect('hromady:home')

    return wrapper_func

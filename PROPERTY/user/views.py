from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm
from .models import CustomUser
from django.contrib.auth.models import User


def reg(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            activate_url = 'http://' + domain + link
            subject = 'Активація акаунту'
            message = activate_url
            sender = 'porchini@ukr.net'
            recipients = form.cleaned_data.get('email')
            mail = send_mail(subject, message, sender, [recipients],
                             fail_silently=False, )
            if mail:
                messages.success(request, 'Підтвердіть пошту для завершення реєстрації ')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/account/registration.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'user/account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    profile = CustomUser.objects.filter(pk=request.user.id)
    title = 'Особистий кабінет'
    return render(request, 'user/profile_view.html', {'profile': profile, 'title': title})


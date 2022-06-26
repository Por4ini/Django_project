from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.views import PasswordChangeView
from hromady.models import CommunityHromady
from .tokens import account_activation_token
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserLoginForm, CustomUserForm
from .models import CustomUser
from django.shortcuts import render
from administrator.models import Request


def reg(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.community_id = '1'
            user.role_id = '1'
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            activate_url = 'http://' + domain + link
            subject = 'Активація акаунту'
            message = f"Вітаємо вас з успішною реєстрацією! \n Для активації аккауту перейдіть по посиланню:  {activate_url}"
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




def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hromady:home')
    else:
        form = UserLoginForm
    return render(request, 'user/account/login.html', {'form': form})

def activate(uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # user_login(request, user)
        return redirect('login')
    else:
        return HttpResponse('Верифікація пройшла успішно.')


def user_logout(request):
    logout(request)
    return redirect('hromady:home')


def profile_view(request):
    profile = CustomUser.objects.filter(pk=request.user.id)
    title = 'Особистий кабінет'
    return render(request, 'user/profile_view.html', {'profile': profile, 'title': title})


def profile_change(request):
    profile = CustomUser.objects.get(id=request.user.id)
    form = CustomUserForm(instance=profile)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    title = 'Редагувати профіль'
    context = {
        "form": form,
        "profile": profile,
        "title": title
    }
    return render(request, 'user/profile_change.html', context)


def change_community(request):
    hromady = CommunityHromady.objects.all()
    title = 'Зміна громади'

    return render(request, 'user/profile_change_com.html', {'title': title, 'hromada': hromady})


def change_community_search(request):
    hromada = CommunityHromady.objects.filter(locality__icontains=request.GET.get("q")[0:4])
    for item in hromada:
        pk = item.id
    data = CustomUser.objects.get(pk=request.user.id)
    title = 'Зміна громади'
    if request.method == 'POST':
        data.community_id = pk
        data.save()

        return redirect('profile')

    return render(request, 'user/profile_change_com_search.html', {'title': title, 'hromada': hromada})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("profile")


def password_success(request):
    profile = CustomUser.objects.filter(pk=request.user.id)
    title = 'Особистий кабінет'
    return render(request, 'user/profile_view.html', {'profile': profile, 'title': title})


def send_request(request):

    data = Request()
    if request.method == "POST":
        data.email = request.user.email
        data.hromada_id = request.user.community_id
        data.save()
        messages.success(request, 'Заявка успішно подана')
        return redirect('profile')

    return render(request, 'user/send_request.html', {})

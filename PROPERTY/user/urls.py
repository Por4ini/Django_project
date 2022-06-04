from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='user/account/password_reset.html'
    ),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='user/account/password_reset_done.html',
    ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='user/account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='user/account/password_reset_complete.html'),
         name='password_reset_complete'

         ),
    path('signup/', views.reg, name='signup')
]

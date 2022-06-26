from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/change/', views.profile_change, name='change'),
    path('profile/send_request/', views.send_request, name='send_request'),
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
         name='password_reset_complete'),
    path('signup/', views.reg, name='signup'),
    path('change/community', views.change_community, name='change_com'),
    path('change/community/search/', views.change_community_search, name='change_com_search'),
    path('change/password/', views.PasswordChangeView.as_view(template_name='user/profile_change.html'),
         name='change_password'),
    path('change/password_success', views.password_success, name='password_change_done'),


]

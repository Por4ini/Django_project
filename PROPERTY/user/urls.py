from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile_view, name='profile')
]

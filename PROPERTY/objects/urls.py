from django.urls import path
from .views import get_objects

urlpatterns = [
    path('', get_objects, name='objects')
]
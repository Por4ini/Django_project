from django.urls import path
from .views import *

urlpatterns = [
    path('hromada/', community, name='hromady'),
    path('', home, name='home' ),
    path('search/', search, name='search')

]

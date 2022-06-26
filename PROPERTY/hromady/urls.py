from django.urls import path
from .views import *

app_name = 'hromady'

urlpatterns = [
    path('search/', community, name='hromady'),
    path('', home, name='home'),
    path('autosuggest/', autosuggest, name='autosuggest'),
    path('<code>/', hromada, name='ret'),

]

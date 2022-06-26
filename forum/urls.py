from django.urls import path
from .views import *

urlpatterns = [
    path('forum', home_forum, name='forum'),
    path('forum/category/<str:pk>', category, ),
    path('forum/category/create/<str:pk>', create_topic),
    path('forum/category/update/<str:pk>', update_topic),
    path('forum/category/delete/<str:pk>', delete_topic),
    path('forum/post/<str:pk>', post, name='post'),
    path('forum/post/create/<str:pk>', create_post),
    path('forum/post/update/<str:pk>', update_post),
    path('forum/post/delete/<str:pk>', delete_post),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('<code>/object/<int:id>/', get_objects, name='object'),
    path('<code>/object/create/', create_object, name='create_object'),
    path('<code>/object/update/<str:pk>/', update_object, name='update_object'),
    path('<code>/object/delete/<str:pk>/', delete_object, name='delete_object'),
    path('<code>/object/image_create/<str:pk>', create_object_image),
    path('<code>/object/image_delete/<str:pk>', delete_object_image),
    path('<code>/object/document_create/<str:pk>', create_object_document),
    path('<code>/object/document_delete/<str:pk>', delete_object_document),
]

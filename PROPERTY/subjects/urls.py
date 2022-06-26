from django.urls import path
from .views import *

urlpatterns = [
    path('<code>/object/subject/<str:pk>', get_subjects, name='subjects'),
    path('<code>/object/subject/create/<str:pk>', create_subject, name='create_subject'),
    path('<code>/object/subject/update/<str:pk>', update_subject, name='update_subject'),
    path('<code>/object/subject/delete/<str:pk>', delete_subject, name='delete_subject'),
    path('<code>/object/subject/image_create/<str:pk>', create_subject_image),
    path('<code>/object/subject/image_delete/<str:pk>', delete_subject_image),
    path('<code>/object/subject/document_create/<str:pk>', create_subject_document),
    path('<code>/object/subject/document_delete/<str:pk>', delete_subject_document),
]

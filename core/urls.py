from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file-uploaded', views.file_uploaded, name='file-uploaded')
]
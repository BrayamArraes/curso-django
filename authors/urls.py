from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('registro/create/', views.registro_create, name='create'),
]

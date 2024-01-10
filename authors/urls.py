from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('registro/create/', views.registro_create, name='registro_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
]

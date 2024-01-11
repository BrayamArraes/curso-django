from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('registro/create/', views.registro_create, name='registro_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/receita/nova', views.criar_receita, name='criar_receita'),
    path('dashboard/receita/delete/', views.dashboard_receita_delete, name='dashboard_receita_delete'),
    path('dashboard/receita/<int:id>/edit/', views.dashboard_receita_edit, name='dashboard_receita_edit'),
]

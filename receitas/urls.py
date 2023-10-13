from django.urls import path
from receitas import views


urlpatterns = [
    path('', views.home),                     # home
    path('receitas/<int:id>/', views.receitas),
]

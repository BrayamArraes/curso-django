from django.urls import path
from receitas import views

app_name = 'receitas'


urlpatterns = [
    path('', views.home, name='home'),                     # home
    path('receitas/<int:id>/', views.receitas, name='receitas'),
]

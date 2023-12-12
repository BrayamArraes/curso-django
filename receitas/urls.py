from django.urls import path
from receitas import views

app_name = 'receitas'


urlpatterns = [
    path('', views.home, name='home'),                     # home
    path('receitas/search/', views.search, name='search'),  # pesquisa
    path('receitas/categoria/<int:categoria_id>/', views.categoria, name='categoria'),  # categoria
    path('receitas/<int:id>/', views.receitas, name='receitas'),
]

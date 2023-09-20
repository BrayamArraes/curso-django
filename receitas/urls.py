from django.urls import path
from receitas.views import home


urlpatterns = [
    path('', home),                     # home
]

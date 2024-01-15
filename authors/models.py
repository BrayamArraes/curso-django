from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    authors = models.OneToOneField(User, on_delete=models.CASCADE)  # ON_DELETE models.cascade quando vc deletar o usuario vc deleta o perfil
    bio = models.TextField(default='', blank=True)

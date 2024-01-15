from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ValidationError
from django.utils.text import slugify
from collections import defaultdict
import os
from django.conf import settings
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class receita(models.Model):
    title = models.CharField(max_length=65, verbose_name='Titulo')  # verbose_name é a msm coisa que o label # noqa
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receitas/cover/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)

# esta funçao é para mostrar o nome da categoria ou receita que colocar
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('receitas:receita', args=(self.id,))

    # deixando a image de um tamanho padrao
    @staticmethod
    def redimensionar_img(image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width < new_width:
            image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

    # esta função faz com que toda slug fique unica
    def save(self, *args, **kwargs):
        if not self.slug:
          slug = f'{slugify(self.title)}' # noqa
          self.slug = slug  # noqa
        saved = super().save(*args, **kwargs)

        # esse if é referente a rediresionamento de imagem
        if self.cover:
            try:
                self.resize_image(self.cover, 840)
            except FileNotFoundError:
                ...

        return saved

    # esta funçao de validação serve para que o usuario nao cria um receita com mesmo nome
    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)

        receita_from_db = receita.objects.filter(
            title__iexact=self.title
        ).first()

        if receita_from_db:
            if receita_from_db.pk != self.pk:
                error_messages['title'].append(
                    'Já existe receita com este titulo'
                )

        if error_messages:
            raise ValidationError(error_messages)

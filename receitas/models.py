from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=65)
# esta funçao é para mostrar o nome da categoria ou receita que colocar
    def __str__(self):
        return self.name
        

class receita(models.Model):
    title = models.CharField(max_length=65)
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
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

# esta funçao é para mostrar o nome da categoria ou receita que colocar
    def __str__(self):
        return self.title

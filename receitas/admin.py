from django.contrib import admin

from .models import Category, receita


class CategoryAdmin(admin.ModelAdmin):
    ...
@admin.register(receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)



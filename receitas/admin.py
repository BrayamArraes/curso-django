from django.contrib import admin

from .models import Category, receita


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published', 'author']
    list_display_links = 'title', 'created_at',
    search_fields = 'id', 'title', 'description', 'slug',
    list_filter = 'category', 'author', 'is_published',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category, CategoryAdmin)

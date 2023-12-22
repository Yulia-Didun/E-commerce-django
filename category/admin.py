"""
Django admin configuration for the 'Category' model.

This module registers the 'Category' model with a custom admin configuration
to enhance the functionality and appearance of the Django admin interface.
"""
from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """Custom admin configuration for the 'Category' model."""
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)

"""
Django admin configuration for the 'Product' model.

This module registers the 'Product' model with a custom admin configuration
to enhance the functionality and appearance of the Django admin interface.
"""
from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """Custom admin configuration for the 'Product' model."""
    list_display = ('product_name',
                    'price',
                    'stock',
                    'category',
                    'modified_at',
                    'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)

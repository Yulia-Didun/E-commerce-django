"""
Django models for managing product categories.

Classes:
- Category: Model representing a product category.
"""
from django.db import models

# Create your models here.

class Category(models.Model):
    """Model representing a category of products."""
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 50, unique = True)
    description = models.TextField(max_length = 250, blank = True)
    category_image = models.ImageField(upload_to = 'images/categories', blank = True)

    class Meta:
        """Meta class for configuring the behavior of the Category model."""
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.category_name)
    
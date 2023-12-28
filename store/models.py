"""Django models for managing products."""
from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.

class Product(models.Model):
    """Model representing a product."""
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=300, blank=True)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_url(self):
        """Returns the URL for the product."""
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return str(self.product_name)

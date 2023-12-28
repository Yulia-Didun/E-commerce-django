from django.db import models
from store.models import Product

# Create your models here.

class Cart(models.Model):
    """Model representing a shopping cart."""
    cart_id = models.CharField(max_length=250, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)


class CartItem(models.Model):
    """Model representing an item in a shopping cart."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        """Calculates and returns the subtotal for the cart item."""
        return self.quantity * self.product.price

    def __str__(self):
        return str(self.product)

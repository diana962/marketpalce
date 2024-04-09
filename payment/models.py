from django.db import models
from django.contrib.auth import get_user_model
from shopping_cart.models import CartItem

User = get_user_model()


class Payment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    visa = models.CharField(max_length=16)
    visa_password = models.CharField(max_length=4)

    cart_items = models.ManyToManyField(CartItem, related_name='payments')

    def total_amount(self):
        total = 0
        for item in self.cart_items.all():
            total += item.price()
        return total

    def __str__(self):
        return f"Payment of {self.total_amount()} made by {self.user.email} at {self.timestamp}"

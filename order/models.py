from django.db import models
from django.contrib.auth.models import User
from product.models import Clothes

class Order(models.Model):
    ORDERED = 1
    PROCESSING = 2
    DELIVERED = 3

    PROCESSING_CHOICES = (
        (ORDERED, 'Ordered'),
        (PROCESSING, 'Processing'),
        (DELIVERED, 'Delivered')
    )

    product = models.ForeignKey(Clothes, related_name='orders', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PROCESSING_CHOICES, default=ORDERED)

    class Meta:
        unique_together = ['owner', 'product']

    def __str__(self):
        return f"{self.product} * {self.quantity} = {self.product.price * self.quantity}"

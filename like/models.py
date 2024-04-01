from django.db import models
from product.models import Clothes

class Like(models.Model):
    owner = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Clothes, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.username} --> {self.product.title}'

    class Meta:
        unique_together = ['owner', 'product']


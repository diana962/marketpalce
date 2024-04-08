from django.contrib.auth import get_user_model
from django.db import models
from product.models import Clothes

User = get_user_model()
class Like(models.Model):
    owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Clothes, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner.username} --> {self.product.title}'

    class Meta:
        unique_together = ['owner', 'product']

class Favorite(models.Model):
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, related_name='favorites', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'clothes']

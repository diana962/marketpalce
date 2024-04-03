from product.models import Clothes
from django.db import models


class Comment(models.Model):
    owner = models.ForeignKey('auth.User', related_name='comments',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Clothes, related_name='comments',
                                on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.product}'

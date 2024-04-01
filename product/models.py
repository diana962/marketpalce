from django.db import models
from catalog.models import Catalog


class Clothes(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1500, blank=True)
    seller = models.ForeignKey('auth.USER', related_name='clothes', on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, related_name='clothes', on_delete=models.SET_NULL, null=True)
    preview = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.seller} - {self.title[:50]}'

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'


class ClothesImage(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Clothes, related_name='images', on_delete=models.CASCADE)

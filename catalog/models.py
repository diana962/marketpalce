from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
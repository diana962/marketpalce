from django.contrib import admin
from product.models import Clothes


@admin.register(Clothes)
class Clothes(admin.ModelAdmin):
    list_display = ('id', 'title', 'catalog')
    # list_display = ['__all__', ]

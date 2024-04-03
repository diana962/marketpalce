from django.contrib import admin
from catalog.models import Catalog


@admin.register(Catalog)
class Catal(admin.ModelAdmin):
    list_display = ['name', 'count']

    def count(self, obj):
        return obj.clothes.count()
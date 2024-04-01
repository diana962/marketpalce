from django.contrib import admin
from catalog.models import Catalog

# admin.site.register(Catalog)
#
@admin.register(Catalog)
class Catal(admin.ModelAdmin):
    list_display = ['name', ]
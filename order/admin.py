from django.contrib import admin
from .models import Order

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'owner', 'quantity', 'summa','status')
    list_filter = ('status', 'created_at')
    search_fields = ('product__name', 'owner__username')

    def summa(self, obj):
        return obj.product.price * obj.quantity

    summa.short_description = 'Sum'


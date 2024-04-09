from django.contrib import admin

from shopping_cart.models import CartItem

# admin.site.register(CartItem)
@admin.register(CartItem)
class Cart(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']

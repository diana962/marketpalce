from django.contrib import admin
from payment.models import Payment

# admin.site.register(Payment)
@admin.register(Payment)
class Pay(admin.ModelAdmin):
    list_display = ['user', 'total_amount', 'timestamp']
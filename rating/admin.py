from django.contrib import admin
from rating.models import Rating
@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'rating')

    def title(self, obj):
        return [obj.product.title]


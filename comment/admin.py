from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class Comm(admin.ModelAdmin):
    list_display = ['product', 'id']
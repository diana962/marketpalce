from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['is_active']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('email', 'first_name', 'last_name')})  ,
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Custom fields'), {'fields': ('activation_code',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

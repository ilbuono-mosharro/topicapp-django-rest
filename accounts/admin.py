from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class AdminUser(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login',)
    fieldsets = (
        ("Account", {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'avatar',)
        }),
        ('Email', {'fields': ('email', 'email_confirmation',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('-date_joined',)

admin.site.register(MyUser, AdminUser)
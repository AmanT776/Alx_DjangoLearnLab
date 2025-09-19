# relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from LibraryProject.bookshelf.admin import CustomUserAdmin
from .models import User, UserProfile,CustomUser,CustomUserAdmin

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (_('Additional Info'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (_('Additional Info'), {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)

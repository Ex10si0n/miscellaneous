from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('DOB',)}),)
    list_display = ['username', 'email', 'DOB']
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)

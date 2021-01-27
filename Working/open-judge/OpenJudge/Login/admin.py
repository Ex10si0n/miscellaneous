from django.contrib import admin
from .models import User

# Model admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment', 'email', 'school')

# Register your models here.
admin.site.register(User, UserAdmin)
from django.contrib import admin
from booktest.models import BookInfo, Character

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'bTitle', 'bPub_date']

class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'hName', 'hGender', 'hComment', 'hBook']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(Character, CharacterAdmin)

from django.contrib import admin
from .models import Save_File


@admin.register(Save_File)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'save_file',)

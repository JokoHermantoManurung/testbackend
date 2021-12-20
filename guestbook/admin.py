from django.contrib import admin
from .models import GuestBook
# Register your models here.

@admin.register(GuestBook)

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat','email')
    search_fields = ('nama', 'alamat', 'email')
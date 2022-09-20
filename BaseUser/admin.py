from django.contrib import admin
from .models import BaseUser
# Register your models here.

@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","last_name","email","is_staff","is_active","date_joined"]
    list_filter = ["is_staff","is_active"]
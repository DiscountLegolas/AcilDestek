from django.contrib import admin
from .models import İl,İlçe
# Register your models here.

@admin.register(İl)
class İlAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(İlçe)
class İlçeAdmin(admin.ModelAdmin):
    list_display=["name","il"]
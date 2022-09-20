from django.contrib import admin
from .models import ServiceCategory
# Register your models here.
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ["name","parent"]
from django.contrib import admin
from .models import PersonalAccount
# Register your models here.
@admin.register(PersonalAccount)
class PersonalAccount(admin.ModelAdmin):
    list_display=["user"]
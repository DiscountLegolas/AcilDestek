from django.contrib import admin
from .models import GuestUser
@admin.register(GuestUser)
class ExpertAdmin(admin.ModelAdmin):
    list_display=["long","lat"]


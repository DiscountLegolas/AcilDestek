from django.contrib import admin
from .models import Expert,OpeningHours,ExpertImage
# Register your models here.
@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display=["user","description","companyname","long","lat"]

@admin.register(OpeningHours)
class OpeningHourseAdmin(admin.ModelAdmin):
    list_display=["company","weekday","from_hour","to_hour","is_closed"]

@admin.register(ExpertImage)
class ExpertImageAdmin(admin.ModelAdmin):
    list_display = ["expert","image","id"]
    list_filter = ("expert",)
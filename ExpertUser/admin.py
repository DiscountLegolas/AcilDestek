from django.contrib import admin
from .models import Expert,OpeningHours
# Register your models here.
@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display=["user","description","companyname","category","long","lat"]

@admin.register(OpeningHours)
class OpeningHourseAdmin(admin.ModelAdmin):
    list_display=["company","weekday","from_hour","to_hour","is_closed"]
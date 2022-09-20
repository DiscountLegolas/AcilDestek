from django.contrib import admin
from .models import ExpertReview
# Register your models here.

@admin.register(ExpertReview)
class ExpertReviewAdmin(admin.ModelAdmin):
    list_display=["user","expert","text","rate","createdDate"]
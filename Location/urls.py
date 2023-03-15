from django.urls import path
from .views import *

app_name="location"
urlpatterns=[
    path('list/',IlAndIlceListAPIView.as_view(),name="list"),
]
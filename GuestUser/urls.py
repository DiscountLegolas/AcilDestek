from django.urls import path
from .views import *

app_name="guestuser"
urlpatterns = [
    path("register/",GuestRegisterCreateApiView.as_view(),name="url_register"),
    path("info/<int:guestid>",GetGuestInfoApiView.as_view(),name="url_register"),
    path("callexpert/",CallExpertCreateApiView.as_view(),name="url_register"),
]

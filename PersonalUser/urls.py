from django.urls import path
from .views import PersonalUserProfileAPIView,PersonalUserRegisterAPIView,CallExpertCreateApiView
from PersonalUser import views

app_name="personaluser"
urlpatterns = [
    path("register/",PersonalUserRegisterAPIView.as_view(),name="url_register"),
    path("profile/<int:customer_id>",PersonalUserProfileAPIView.as_view()),
    path("callexpert/",CallExpertCreateApiView.as_view(),name="url_register"),
]

from django.urls import path
from .views import ExpertUserProfileAPIView,ExpertUserRegisterAPIView,OpeningHoursCreateApiView
from PersonalUser import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name="expertuser"
urlpatterns = [
    path("register/",ExpertUserRegisterAPIView.as_view(),name="url_register"),
    path("profile/<int:id>",ExpertUserProfileAPIView.as_view()),
    path("profile/addhours/",ExpertUserProfileAPIView.as_view()),   
]

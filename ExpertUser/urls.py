from django.urls import path
from .views import ExpertUserProfileAPIView,ExpertUserRegisterAPIView,OpeningHoursCreateApiView,OpeningHoursUpdateApiView
from PersonalUser import views
from rest_framework.routers import DefaultRouter

app_name="expertuser"
urlpatterns = [
    path("register/",ExpertUserRegisterAPIView.as_view(),name="url_register"),
    path("profile/<int:id>",ExpertUserProfileAPIView.as_view()),
    path("profile/addhours/",OpeningHoursCreateApiView.as_view()),
    path("profile/updatehours/<int:pk>",OpeningHoursUpdateApiView.as_view()),   

]

from django.urls import path
from .views import ExpertUserProfileAPIView,ExpertUserRegisterAPIView
from PersonalUser import views

app_name="personaluser"
urlpatterns = [
    path("register/",ExpertUserRegisterAPIView.as_view(),name="url_register"),
    path("profile/<int:id>",ExpertUserProfileAPIView.as_view()),   
]

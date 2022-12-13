from django.urls import path
from .views import SendMessageAPIView
from PersonalUser import views

app_name="messaging"
urlpatterns = [
    path("sendmessage/",SendMessageAPIView.as_view(),name="url_send"),
    ]
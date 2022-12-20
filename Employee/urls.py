from django.urls import path
from .views import EmployeeRegisterAPIView
from Employee import views

app_name="employee"
urlpatterns = [
    path("register/",EmployeeRegisterAPIView.as_view(),name="url_register"),
]

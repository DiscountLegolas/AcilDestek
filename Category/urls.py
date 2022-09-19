from django.urls import path
from .views import GetAllCategoriesAPIView

app_name="category"
urlpatterns = [
    path("list/",GetAllCategoriesAPIView.as_view(),name="url_categorylist"),
]

from django.urls import path
from .views import GetAllCategoriesAPIView,GetCategoryDetailsAPIView

app_name="category"
urlpatterns = [
    path("list/",GetAllCategoriesAPIView.as_view(),name="url_categorylist"),
    path("detail/<int:id>",GetCategoryDetailsAPIView.as_view(),name="url_category_detail"),
]

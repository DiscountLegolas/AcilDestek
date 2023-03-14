from django.urls import path, re_path
from Favourite.views import FavCreateAPIView,FavListAPIView,FavDeleteAPIView

app_name="favourite"
urlpatterns = [
    re_path(r'^list/$',FavListAPIView.as_view(),name='list'),
    path('create/',FavCreateAPIView.as_view(),name='create'),
    path('delete/<pk>',FavDeleteAPIView.as_view(),name="delete"),
]
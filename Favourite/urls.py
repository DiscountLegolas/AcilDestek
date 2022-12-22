from django.urls import path
from Favourite.views import FavCreateAPIView,FavListAPIView,FavDeleteAPIView

app_name="favourite"
urlpatterns = [
    path('list/',FavListAPIView.as_view(),name='list'),
    path('create/',FavCreateAPIView.as_view(),name='create'),
    path('delete/<pk>',FavDeleteAPIView.as_view(),name="delete"),
]
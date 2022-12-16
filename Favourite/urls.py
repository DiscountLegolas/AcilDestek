from django.urls import path
from Favourite.views import FavListCreateAPIView,FavDeleteAPIView

app_name="favourite"
urlpatterns = [
    path('list-create/',FavListCreateAPIView.as_view(),name='list-create'),
    path('delete/<pk>',FavDeleteAPIView.as_view(),name="delete"),
]
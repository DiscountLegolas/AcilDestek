from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from Favourite.models import UserFavExpert
from Favourite.serializers import FavListSerializer,FavCreateSerializer,FavDeleteSerializer
# Create your views here.



class FavListAPIView(ListAPIView):

    queryset = UserFavExpert.objects.all()
    serializer_class = FavListSerializer

class FavCreateAPIView(CreateAPIView):

    queryset = UserFavExpert.objects.all()
    serializer_class = FavCreateSerializer

class FavDeleteAPIView(DestroyAPIView):
    queryset = UserFavExpert.objects.all()
    serializer_class = FavDeleteSerializer
    lookup_field = 'pk'

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
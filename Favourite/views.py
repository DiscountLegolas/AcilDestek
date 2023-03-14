from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from Favourite.models import UserFavExpert
from Favourite.serializers import *
from rest_framework.exceptions import APIException

# Create your views here.



class FavListAPIView(ListAPIView):
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return GuestUserFavExpert.objects.filter(user__id=self.request.GET.get("guestid"))
        elif self.request.user.role==2:
            return UserFavExpert.objects.filter(user=self.request.user)
        raise APIException("You Must Be customer or guest")
    
    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return GuestFavListSerializer
        elif self.request.user.role==2:
            return FavListSerializer
        raise APIException("You Must Be customer or guest")


class FavCreateAPIView(CreateAPIView):

    queryset = UserFavExpert.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return GuestFavCreateSerializer
        elif self.request.user.role==2:
            return FavCreateSerializer
        raise APIException("You Must Be customer or guest")

class FavDeleteAPIView(DestroyAPIView):
    queryset = UserFavExpert.objects.all()
    lookup_field = 'pk'
    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return GuestFavDeleteSerializer
        elif self.request.user.role==2:
            return FavDeleteSerializer
        raise APIException("You Must Be customer or guest")
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
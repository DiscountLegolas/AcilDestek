from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from Favourite.models import UserFavExpert
from Favourite.serializers import FavListCreateSerializer,FavDeleteSerializer
# Create your views here.



class FavListCreateAPIView(ListCreateAPIView):

    serializer_class = FavListCreateSerializer

    def get_queryset(self):
        return UserFavExpert.objects.filter(user = self.request.user.id)
        
    def perform_create(self, serializer):
        return serializer.save(user= serializer.validated_data['user'])

class FavDeleteAPIView(DestroyAPIView):
    queryset = UserFavExpert.objects.all()
    serializer_class = FavDeleteSerializer
    lookup_field = 'pk'

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
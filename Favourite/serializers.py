from rest_framework.serializers import ModelSerializer
from Favourite.models import *

class GuestFavListSerializer(ModelSerializer):
    class Meta:
        model = GuestUserFavExpert
        fields = ('user','expert',)

class GuestFavCreateSerializer(ModelSerializer):
    class Meta:
        model = GuestUserFavExpert
        fields = ('user','expert',)
    
class GuestFavDeleteSerializer(ModelSerializer):
    class Meta:
        model = GuestUserFavExpert
        fields = ['pk']
class FavListSerializer(ModelSerializer):
    class Meta:
        model = UserFavExpert
        fields = ('user','expert',)

class FavCreateSerializer(ModelSerializer):
    class Meta:
        model = UserFavExpert
        fields = ('user','expert',)
    
class FavDeleteSerializer(ModelSerializer):
    class Meta:
        model = UserFavExpert
        fields = ['pk']
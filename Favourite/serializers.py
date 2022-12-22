from rest_framework.serializers import ModelSerializer
from Favourite.models import UserFavExpert

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
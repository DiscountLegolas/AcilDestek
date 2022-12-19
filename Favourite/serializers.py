from rest_framework.serializers import ModelSerializer
from Favourite.models import UserFavExpert

class FavListCreateSerializer(ModelSerializer):
    class Meta:
        model = UserFavExpert
        fields = ('user','expert',)
    
class FavDeleteSerializer(ModelSerializer):
    class Meta:
        model = UserFavExpert
        fields = ['pk']
from rest_framework import serializers
from .models import *


class İlSerializer(serializers.ModelSerializer):
    class Meta:
        model = İl
        fields=("name",)

class İlçeSerializer(serializers.ModelSerializer):
    class Meta:
        model = İlçe
        fields=("name",)

class IlAndIlceListSerializer(serializers.ModelSerializer):
    ilceler = İlçeSerializer(many=True)
    class Meta:
        model = İl
        fields = ('name','ilceler')
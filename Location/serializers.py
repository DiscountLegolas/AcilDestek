from rest_framework import serializers
from .models import *


class İlSerializer(serializers.ModelSerializer):
    class Meta:
        model = İl
        fields=("name")

class İlçeSerializer(serializers.ModelSerializer):
    il=İlSerializer()
    class Meta:
        model = İlçe
        fields=("name","il")
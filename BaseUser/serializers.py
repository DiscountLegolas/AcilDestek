from .models import BaseUser
from Location.serializers import İlçeSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class BaseUserSerializer(serializers.ModelSerializer):

    il=serializers.CharField(source="il.name")

    ilçe=serializers.CharField(source="ilçe.name")
    class Meta:
        model = BaseUser
        fields= ( "id" , "first_name","last_name","email","phone","il","ilçe")


class BaseUserRegisterSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(required=True,validators=[UniqueValidator(queryset=BaseUser.objects.all())])
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=BaseUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True)
    il=serializers.CharField(required=True)
    ilçe=serializers.CharField(required=True)
    class Meta:
        model = BaseUser
        fields= (  "first_name","password","last_name","email","phone","il","ilçe")
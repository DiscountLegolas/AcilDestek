from .models import BaseUser
from Location.serializers import İlçeSerializer
from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from GuestUser.models import GuestUser
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class CallExpertSerializer(serializers.Serializer):
        callerid = serializers.IntegerField()
        calledexpertphone = serializers.CharField(max_length=200)
        def create(self, validated_data):
            if self.context["request"].user.is_anonymous:
                gu=GuestUser.objects.get(id==validated_data['callerid'])
                gu.previusexpertcalls.add(Expert.objects.get(user__phone=validated_data['calledexpertphone']))
                return gu
 
            else:
                c=PersonalAccount.objects.get(id==validated_data['callerid'])
                c.previusexpertcalls.add(Expert.objects.get(user__phone=validated_data['calledexpertphone']))
                return c


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
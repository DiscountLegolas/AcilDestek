import json
from types import SimpleNamespace
from Category.serializers import *
from django.contrib.sites.shortcuts import get_current_site 
from .models import Expert
from rest_framework import serializers
from BaseUser.models import BaseUser
from BaseUser.serializers import *
from Location.models import *
from django.contrib.auth.hashers import make_password

class SerializerExpertProfile(serializers.ModelSerializer):
    
    user=BaseUserSerializer()
    class Meta:
        model  = Expert
        fields = "__all__"


class RegisterExpertSerializer(serializers.ModelSerializer):

    user=BaseUserRegisterSerializer()
    description=serializers.CharField(required=True)
    companyname=serializers.CharField(required=True)
    category=serializers.CharField(required=True)
    openingtime=serializers.TimeField(required=True)
    closingtime=serializers.TimeField(required=True)
    long = serializers.DecimalField(max_digits=9, decimal_places=6)
    lat  =  serializers.DecimalField(max_digits=9, decimal_places=6)
    class Meta:
        model = BaseUser
        fields = ('user','category','long',"lat","description","companyname","openingtime","closingtime")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone':{'required':True},
        }
    def create(self, validated_data):
        userdict=validated_data["user"]
        user = BaseUser.objects.create(
            first_name   = userdict['first_name'],
            password=make_password(userdict['password']),
            email      = userdict['email'],
            last_name  = userdict['last_name'],
            phone=userdict['phone'],
            is_expert=True,
            il=İl.objects.get(name=userdict['il']),
            ilçe=İlçe.objects.get(name=userdict['ilçe'])
        )
        user.set_password(userdict['password'])
        user.sendactivationmail(get_current_site(self.context['request']))
        user.save()
        expert=Expert.objects.create(user=user,long=validated_data['long'],lat=validated_data["lat"],category=ServiceCategory.objects.get(name=validated_data['category']),description=validated_data['description'],companyname=validated_data['companyname'],openingtime=validated_data['openingtime'],closingtime=validated_data['closingtime'])
        return expert

class SerializerExpertSimpleInfo(serializers.ModelSerializer):
    email=serializers.SerializerMethodField()
    namesurname=serializers.SerializerMethodField()
    id=serializers.IntegerField(source="user.id")

    def get_email(self,obj):
        return obj.user.email
    def get_namesurname(self,obj):
        return obj.user.name_surname()
    

    class Meta:
        model  = Expert
        fields = ("id","namesurname","phone","averagescore")
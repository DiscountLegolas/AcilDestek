import email
from django.contrib.sites.shortcuts import get_current_site
from .models import PersonalAccount
from rest_framework import serializers
from BaseUser.models import BaseUser
from BaseUser.serializers import *
from rest_framework.validators import UniqueValidator
from Location.models import *
from django.contrib.auth.hashers import make_password

class SerializerPersonalUserProfile(serializers.ModelSerializer):


    user=BaseUserSerializer()

    
    class Meta:
        model  = PersonalAccount
        fields = "__all__"


class RegisterUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    il=serializers.CharField(required=True)
    ilçe=serializers.CharField(required=True)
    class Meta:
        model = BaseUser
        fields = ('id','first_name', 'last_name', 'email','phone', 'password','il','ilçe')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone':{'required':True}
        }
    def create(self, validated_data):
        user=None
        if BaseUser.objects.filter(email=validated_data['email'],is_regular=True).exists():
            raise serializers.ValidationError("An Customer With This Email Already exists you can try to create different account types")
        elif BaseUser.objects.filter(email=validated_data['email']).exists()==False:
            user=BaseUser.objects.create(
                first_name   = validated_data['first_name'],
                password=make_password(validated_data['password']),
                email      = validated_data['email'],
                last_name  = validated_data['last_name'],
                phone=validated_data['phone'],
                is_regular=True,
                il=İl.objects.get(name=validated_data['il']),
                ilçe=İlçe.objects.get(name=validated_data['ilçe'])
            )
            user.sendactivationmail(get_current_site(self.context['request']))
        user=BaseUser.objects.filter(email=validated_data['email']).first() if user is None else user
        user.is_regular=True
        user.save()
        user.sendactivationmail(get_current_site(self.context['request']))
        personaluser=PersonalAccount.objects.create(user=user)
        return user


class SerializerPersonalUserCommentInfo(serializers.ModelSerializer):

    namesurname=serializers.SerializerMethodField()
    email=serializers.CharField(source="user.email")
    phone=serializers.CharField(source="user.phone")
    id = serializers.IntegerField(source="user.id")
    

    def get_namesurname(self,obj):
        fn=obj.user.first_name
        ln=obj.user.last_name
        fn=fn[0]+'*'*(len(fn)-1)
        ln=ln[0]+'*'*(len(fn)-1)
        return fn+" "+ln

    class Meta:
        model  = PersonalAccount
        fields = ["id","email","phone","namesurname",]

class SerializerPersonalUserSimpleInfo(serializers.ModelSerializer):


    namesurname=serializers.SerializerMethodField()
    email=serializers.CharField(source="user.email")
    phone=serializers.CharField(source="user.phone")
    id = serializers.IntegerField(source="user.id")
    

    def get_namesurname(self,obj):
        return obj.user.name_surname()

    class Meta:
        model  = PersonalAccount
        fields = ["id","email","phone","namesurname",]
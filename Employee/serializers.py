from django.contrib.sites.shortcuts import get_current_site
from .models import Employee
from rest_framework import serializers
from BaseUser.models import BaseUser
from ExpertUser.models import Expert
from BaseUser.serializers import *
from rest_framework.validators import UniqueValidator
from Location.models import *
from django.contrib.auth.hashers import make_password

class RegisterEmployeeSerializer(serializers.ModelSerializer):
    employer=serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    il=serializers.CharField(required=True)
    ilçe=serializers.CharField(required=True)
    class Meta:
        model = BaseUser
        fields = ('id','employer','first_name', 'last_name', 'email','phone', 'password','il','ilçe')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone':{'required':True}
        }
    def create(self, validated_data):
        user=None
        pw=validated_data['password']
        if BaseUser.objects.filter(email=validated_data['email'],is_employee=True).exists():
            serializers.ValidationError("An Employee With This Email Already exists you can try to create different account types")
        elif BaseUser.objects.filter(email=validated_data['email']).exists()==False:
            baseuserserializer = BaseUserRegisterSerializer(context={'site': get_current_site(self.context['request'])})
            user=baseuserserializer.create(validated_data)
        user=BaseUser.objects.filter(email=validated_data['email']).first() if user is None else user
        user.is_employee=True
        user.save()
        user.sendactivationmail(get_current_site(self.context['request']))
        employer=Employee.objects.create(user=user,employer=Expert.objects.filter(companyname=validated_data['employer']).first(),password=make_password(pw))
        return user
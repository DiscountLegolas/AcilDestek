from django.contrib.sites.shortcuts import get_current_site
from Location.models import İl,İlçe
from .models import BaseUser
from . import google
from .google import social_user
from rest_framework.exceptions import AuthenticationFailed
import os
from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from GuestUser.models import GuestUser
from Employee.models import Employee
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode



class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return social_user(
            provider=provider, user_id=user_id, email=email, name=name)


class ProfileSerializer(serializers.Serializer):
    profiles=serializers.SerializerMethodField()

    def get_profiles(self, instance):
        profiles={}
        
        user=self.context["request"].user
        profiles["expert"] =Expert.objects.get(user=user).companyname if Expert.objects.filter(user=user).exists() else None
        profiles["customer"]= user.first_name if PersonalAccount.objects.filter(user=user).exists() else None
        profiles["employee"]=user.first_name if Employee.objects.filter(user=user).exists() else None
        return profiles



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

    il=serializers.CharField(source="il.name",default=None) # added default name
    ilçe=serializers.CharField(source="ilçe.name",default=None)
    class Meta:
        model = BaseUser
        fields= ( "id" , "first_name","last_name","email","phone","il","ilçe")

class AccountTypesSerializer(serializers.Serializer):
    emailistaken=serializers.BooleanField()
    emailisvalid=serializers.BooleanField()
    expertprofileexists=serializers.BooleanField()
    customerprofileexists=serializers.BooleanField()
    employeeprofileexists=serializers.BooleanField()

class BaseUserRegisterSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    il=serializers.CharField(required=False)
    ilçe=serializers.CharField(required=False)
    def create(self, validated_data,):
        passw=validated_data.pop("password",None)
        il=validated_data.pop("il",None)
        ilçe=validated_data.pop("ilçe",None)
        user=BaseUser.objects.create(
            **validated_data,
            il=İl.objects.get(name=il) if il is not None else None,
            ilçe=İlçe.objects.get(name=ilçe) if ilçe is not None else None
        )
        user.sendactivationmail(self.context['site'])
        return user
    class Meta:
        model = BaseUser
        fields= (  "first_name","last_name","email","phone","il","ilçe","password")



class BaseUserUpdateSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(required=False,default="")
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    il=serializers.CharField(required=False)
    ilçe=serializers.CharField(required=False)
    class Meta:
        model = BaseUser
        fields= (  "first_name","last_name","email","phone","il","ilçe","password")



class EmailSerializer(serializers.Serializer):

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)


class OtpEmailSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    class Meta:
        fields = ("email",)



class ResetPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = BaseUser.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data
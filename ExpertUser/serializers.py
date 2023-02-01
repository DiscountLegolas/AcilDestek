from rest_framework.response import Response
from Category.serializers import *
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.sites.shortcuts import get_current_site
from Comment.models import ExpertReview 
from .models import Expert, ExpertImage, OpeningHours
from rest_framework import serializers
from BaseUser.models import BaseUser
from BaseUser.serializers import *
from Location.models import *
from django.contrib.auth.hashers import make_password

class ExpertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertImage
        fields = ('image',)
        



class ImageListSerializer ( serializers.Serializer ) :
    image = serializers.ListField(child=serializers.FileField( max_length=100000,allow_empty_file=False,use_url=False ),write_only=True)

    def create(self, validated_data):
        image=validated_data.pop('image')
        for img in image:
            expertimage=ExpertImage.objects.create(image=img,expert=Expert.objects.get(user=self.context["request"].user))
        return Response({"Success": "Resimleriniz oluşturuldu"})
        

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = (
                'weekday',
                'from_hour',
                'to_hour',
                'is_closed'
            )

                
class UpdateOpeningHoursSerializer(serializers.Serializer):
    openinghours = OpeningHoursSerializer(many=True,write_only=True)
    responselist=serializers.SerializerMethodField()

    def get_responselist(self,obj):
        ohlist=OpeningHours.objects.filter(company=Expert.objects.get(user=self.context["request"].user)).values('weekday','from_hour','to_hour','is_closed')
        return ohlist



    def create(self, validated_data,*args,**kwargs):
        for openinghour in validated_data['openinghours']:
            oh=OpeningHours.objects.get(company=Expert.objects.get(user=self.context["request"].user),weekday=openinghour["weekday"])
            jsonstr=json.dumps(openinghour,cls=DjangoJSONEncoder)
            my_data =json.loads(jsonstr)
            keys = list(my_data.keys())
            for key in keys:
                setattr(oh, key, my_data[key])
                    
            oh.save(update_fields=keys)


class SerializerExpertProfile(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField()
    expertimages=ExpertImageSerializer(many=True)

    def get_reviews(self,obj):
        newarr = [{'created_date': i.createdDate,'text':i.text,'rate':i.rate,'fullname':i.customernamesurname} for i in ExpertReview.objects.filter(expert__user__id=self.context['view'].kwargs.get("id"), user__isnull=False)]
        return newarr

    
    user=BaseUserSerializer()
    class Meta:
        model  = Expert
        fields = ('user',"description","companyname","countofreviews","averagescore","workinghours","expertimages","reviews","long","lat")


class SerializerExpertProfileF(serializers.ModelSerializer):
    reviews=serializers.SerializerMethodField()
    expertimages=ExpertImageSerializer(many=True)
    isaddedtofavorites=serializers.SerializerMethodField()

    def get_reviews(self,obj):
        newarr = [{'created_date': i.createdDate,'text':i.text,'rate':i.rate,'fullname':i.customernamesurname} for i in ExpertReview.objects.filter(expert__user__id=self.context['view'].kwargs.get("id"), user__isnull=False)]
        return newarr

    def get_isaddedtofavorites(self,obj):
        return self.context["request"].user.favorites.filter(expert=obj).exists()

    user=BaseUserSerializer()
    class Meta:
        model  = Expert
        fields = ('user',"description","companyname","countofreviews","averagescore","workinghours","expertimages","reviews","long","lat","isaddedtofavorites",)

class RegisterExpertSerializer(serializers.ModelSerializer):

    user=BaseUserRegisterSerializer()
    description=serializers.CharField(required=True)
    companyname=serializers.CharField(required=True)
    category = serializers.CharField(required=False)
    long = serializers.DecimalField(max_digits=9, decimal_places=6)
    lat  =  serializers.DecimalField(max_digits=9, decimal_places=6)
    workinghours = OpeningHoursSerializer(many=True,write_only=False,default=[])

    class Meta:
        model = BaseUser
        fields = ('user','long',"lat","description","companyname","workinghours","category")

        
    def create(self, validated_data):
        user=None
        wh=validated_data.pop("workinghours",None)
        cat=validated_data.pop("category",None)
        userdict=validated_data.pop("user",None)
        if BaseUser.objects.filter(email=userdict['email'],is_expert=True).exists():
            raise serializers.ValidationError("An Expert With This Email Already exists you can try to create different account types")
        elif BaseUser.objects.filter(email=userdict['email']).exists()==False:
            baseuserserializer = BaseUserRegisterSerializer(context={'site': get_current_site(self.context['request'])})
            user=baseuserserializer.create(userdict)
        user=BaseUser.objects.filter(email=userdict['email']).first() if user is None else user
        user.is_expert=True
        expert=Expert.objects.create(user=user,password=make_password(userdict["password"]),category=ServiceCategory.objects.get(name=cat) if "category" in validated_data else None,**validated_data)
        for openinghour in wh:
            OpeningHours.objects.create(company=Expert.objects.get(user=self.context["request"].user),**openinghour)
        return expert


class UpdateExpertSerializer(serializers.ModelSerializer):

    workinghours = OpeningHoursSerializer(many=True,write_only=False,default=[])
    image = serializers.ListField(child=serializers.FileField( max_length=100000,allow_empty_file=False,use_url=False ),write_only=True,default=[])

    class Meta:
        model = Expert
        fields = ('user','long',"lat","description","companyname","category","workinghours","expertimages")

    def update(self,instance,  validated_data):
        user=self.context["request"].user
        wh=validated_data.pop("workinghours",None)
        cat=validated_data.pop("category",None)
        userdict=validated_data.pop("user",None)
        user.update(**userdict)

        expert=Expert.objects.update(category=ServiceCategory.objects.get(name=validated_data["category"]) if "category" in validated_data else None,**validated_data)
        for openinghour in wh:
            oh=OpeningHours.objects.get(company=Expert.objects.get(user=self.context["request"].user),weekday=openinghour["weekday"])
            jsonstr=json.dumps(openinghour,cls=DjangoJSONEncoder)
            my_data =json.loads(jsonstr)
            keys = list(my_data.keys())
            for key in keys:
                setattr(oh, key, my_data[key])        
            oh.save(update_fields=keys)
        image=validated_data.pop('image')
        for img in image:
            expertimage=ExpertImage.objects.create(image=img,expert=Expert.objects.get(user=user))
        return expert

class SerializerExpertSimpleInfo(serializers.ModelSerializer):
    phone=serializers.SerializerMethodField()
    id=serializers.IntegerField(source="user.id",required=False)
    expertimages=ExpertImageSerializer(many=True,required=False)

    def get_phone(self,obj):
        return obj.user.phone


    class Meta:
        model  = Expert
        fields = ("id","description","phone","companyname","countofreviews","averagescore","expertimages","openorclose")



class SerializerExpertSimpleInfoF(serializers.ModelSerializer):
    isaddedtofavorites=serializers.SerializerMethodField()
    id=serializers.IntegerField(source="user.id",required=False)
    expertimages=ExpertImageSerializer(many=True,required=False)
    phone=serializers.SerializerMethodField()

    def get_phone(self,obj):
        return obj.user.phone
    def get_isaddedtofavorites(self,obj):
        print(obj.user.favorites)
        return self.context["request"].user.favorites.filter(expert=obj).exists()


    class Meta:
        model  = Expert
        fields = ("id","description","phone","companyname","countofreviews","averagescore","expertimages","openorclose","isaddedtofavorites")
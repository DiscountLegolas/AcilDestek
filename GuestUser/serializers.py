from rest_framework import serializers

from ExpertUser.models import Expert
from .models import GuestUser


class GuestRegisterSerializer(serializers.Serializer):
    long = serializers.DecimalField(max_digits=9, decimal_places=6,required=True)
    lat  =  serializers.DecimalField(max_digits=9, decimal_places=6,required=True)
    def create(self, validated_data):
        gu=GuestUser.objects.create(long=validated_data['long'],lat=validated_data["lat"])
        return gu




class GuestSerializer(serializers.ModelSerializer):
    id = serializers.Field()

    class Meta:
        model  = GuestUser
        fields = "__all__"

class GuestCallExpertSerializer(serializers.Serializer):
        callerid = serializers.IntegerField()
        calledexpertphone = serializers.CharField(max_length=200)
        def create(self, validated_data):
            gu=GuestUser.objects.get(id==validated_data['callerid'])
            gu.previusexpertcalls.add(Expert.objects.get(user__phone=validated_data['calledexpertphone']))
            return gu

from rest_framework import serializers

from ExpertUser.models import Expert
from .models import GuestUser

class GuestSerializer(serializers.ModelSerializer):
    
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

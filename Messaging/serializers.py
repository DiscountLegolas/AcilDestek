from rest_framework import serializers
from .models import Message
from BaseUser.models import BaseUser


class SerializerSendMessage(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=("sender","reciever","msg_content")


    def create(self, validated_data):
        return Message.objects.create(sender=validated_data["sender"], reciever=validated_data["reciever"],msg_content=validated_data['msg_content'])

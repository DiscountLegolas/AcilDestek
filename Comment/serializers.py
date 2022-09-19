from rest_framework import serializers
from Comment.models import ExpertReview
from PersonalUser.serializers import *
from ExpertUser.models import *

 

class SerializerCreateExpertReview(serializers.ModelSerializer):
    class Meta:
        model  = ExpertReview
        fields = ("text","rate")

    def create(self, validated_data):
        usta = Expert.objects.get(id=self.context['view'].kwargs.get('expert_id'))
        return ExpertReview.objects.create(user=self.context["request"].user, text=validated_data["text"],rate=validated_data["rate"],expert=usta)

class SerializerExpertReviewListByExpert(serializers.ModelSerializer):
    user = SerializerPersonalUserSimpleInfo()

    class Meta:
        model  = ExpertReview
        fields = ("user","text","expert","createdDate","rate")

class SerializerDeleteExpertReview(serializers.ModelSerializer):
    
    class Meta:
        model  = ExpertReview
        fields = ("user")
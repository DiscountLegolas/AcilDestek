from xml.parsers.expat import model
from rest_framework import serializers

from Category.models import ServiceCategory
class SerializerServiceCategoryList(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    class Meta:
        model=ServiceCategory
        fields=('name',)

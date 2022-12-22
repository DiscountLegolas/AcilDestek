from xml.parsers.expat import model
from rest_framework import serializers

from Category.models import ServiceCategory
class SerializerServiceCategoryList(serializers.ModelSerializer):
    class Meta:
        model=ServiceCategory
        fields=('name','parent',)

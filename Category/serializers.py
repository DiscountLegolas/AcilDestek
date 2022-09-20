from xml.parsers.expat import model
from rest_framework import serializers
from mptt.fields import TreeNodeChoiceField

from Category.models import ServiceCategory
class SerializerServiceCategoryList(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    parent = TreeNodeChoiceField(queryset=ServiceCategory.objects.all())
    class Meta:
        model=ServiceCategory
        fields=('name','parent')
from xml.parsers.expat import model
from rest_framework import serializers

from Category.models import ServiceCategory

class SerializerServiceCategoryList(serializers.ModelSerializer):
    class Meta:
        model=ServiceCategory
        fields=('id','name','parent','expertcount')


class SerializerSubServiceCategory(serializers.ModelSerializer):
    class Meta:
        model=ServiceCategory
        fields=('id','name','expertcount')

class SerializerServiceCategoryParent(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    def get_parent(self, obj):
        if obj.parent is not None:
            return SerializerServiceCategoryParent(obj.parent).data
        else:
            return None
            
    class Meta:
        model=ServiceCategory
        fields=('id','name','parent','expertcount')

class SerializerServiceCategoryDetail(serializers.ModelSerializer):
    parent = SerializerServiceCategoryParent()
    subcategories=serializers.SerializerMethodField()
    def get_subcategories(self, obj):
        return SerializerSubServiceCategory(obj.subcategories(),many=True).data
    
    class Meta:
        model=ServiceCategory
        fields=('id','name','parent','expertcount','subcategories')
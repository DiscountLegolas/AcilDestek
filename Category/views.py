from rest_framework.generics import ListAPIView
from Category.models import ServiceCategory
from .serializers import SerializerServiceCategoryList,SerializerServiceCategoryDetail
from .pagination import CategoryPagination
from rest_framework.permissions import IsAuthenticated


class GetAllCategoriesAPIView(ListAPIView):
    serializer_class   = SerializerServiceCategoryList
    pagination_class=CategoryPagination

    def get_queryset(self):
        return ServiceCategory.objects.all()

class GetCategoryDetailsAPIView(ListAPIView):
    serializer_class   = SerializerServiceCategoryDetail

    def get_queryset(self):
        return ServiceCategory.objects.filter(id=self.kwargs.get("id"))

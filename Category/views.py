from rest_framework.generics import ListAPIView
from Category.models import ServiceCategory
from .serializers import SerializerServiceCategoryList
from .pagination import CategoryPagination
from rest_framework.permissions import IsAuthenticated


class GetAllCategoriesAPIView(ListAPIView):
    serializer_class   = SerializerServiceCategoryList
    pagination_class=CategoryPagination

    def get_queryset(self):
        return ServiceCategory.objects.all()

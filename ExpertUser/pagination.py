from rest_framework.pagination import PageNumberPagination

class ExpertPagination(PageNumberPagination):
    page_size = 11
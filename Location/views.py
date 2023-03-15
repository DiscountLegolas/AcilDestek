from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import İl
from .serializers import IlAndIlceListSerializer
# Create your views here.

class IlAndIlceListAPIView(ListAPIView):
    queryset = İl.objects.all()
    serializer_class = IlAndIlceListSerializer
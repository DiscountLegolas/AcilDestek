from rest_framework.permissions import AllowAny,IsAuthenticated
from ExpertUser.models import *
from BaseUser.permissions import IsExpert
from BaseUser.permissions import IsCustomer
from .serializers import *
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from rest_framework import viewsets
from rest_framework import generics

from rest_framework.parsers import *

class UploadExpertPhoto(viewsets.ModelViewSet):
    schema=None
    permission_classes=[IsAuthenticated,IsExpert]
    parser_classes = (MultiPartParser,FormParser,)
    serializer_class = ImageListSerializer
    queryset=ExpertImage.objects.all()


class ExpertUserProfileAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertProfile
    def get_queryset(self):
        return Expert.objects.filter(user__id=self.kwargs.get("id"))

class ExpertUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterExpertSerializer
    queryset = Expert.objects.all()

class CategoriesSetApiView(CreateAPIView):
    permission_classes=[IsAuthenticated,IsExpert]
    serializer_class = AddCategoriesSerializer
    queryset=ServiceCategory.objects.all()


class OpeningHoursCreateApiView(CreateAPIView):
    permission_classes=[IsAuthenticated,IsExpert]
    serializer_class = CreateOpeningHoursSerializer
    queryset=OpeningHours.objects.all()


class OpeningHoursUpdateApiView(CreateModelMixin,viewsets.GenericViewSet):
    permission_classes=[IsAuthenticated,IsExpert]
    queryset=OpeningHours.objects.all()
    def get_serializer_class(self):
        return UpdateOpeningHoursSerializer

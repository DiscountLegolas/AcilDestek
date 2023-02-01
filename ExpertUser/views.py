from rest_framework.permissions import AllowAny,IsAuthenticated
from ExpertUser.models import *
from BaseUser.permissions import IsExpert
from BaseUser.permissions import IsCustomer
from .serializers import *
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView
from rest_framework import viewsets
from rest_framework import generics,status

from rest_framework.parsers import *

class UploadExpertPhoto(viewsets.ModelViewSet):
    schema=None
    permission_classes=[IsAuthenticated,IsExpert]
    parser_classes = (MultiPartParser,FormParser,)
    serializer_class = ImageListSerializer
    queryset=ExpertImage.objects.all()


class ExpertUserProfileAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializers_classes=(SerializerExpertProfileF,SerializerExpertProfile)
    def get_queryset(self):
        return Expert.objects.filter(user__id=self.kwargs.get("id"))

    
    def list(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            self.serializer_class = self.serializers_classes[1]
            return super().list(request, *args, **kwargs)

        self.serializer_class = self.serializers_classes[0]
        return super().list(request, *args, **kwargs)

class ExpertUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterExpertSerializer
    queryset = Expert.objects.all()




class OpeningHoursUpdateApiView(CreateModelMixin,viewsets.GenericViewSet):
    permission_classes=[IsAuthenticated,IsExpert]
    queryset=OpeningHours.objects.all()
    def get_serializer_class(self):
        return UpdateOpeningHoursSerializer

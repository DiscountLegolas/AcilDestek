from rest_framework.permissions import AllowAny,IsAuthenticated
from ExpertUser.models import *
from BaseUser.permissions import IsExpert
from .serializers import *
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from rest_framework import viewsets
from rest_framework import generics

from rest_framework.parsers import *
from ExpertUser.serializers import ImageListSerializer

class UploadExpertPhotos(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,IsExpert]
    serializer_class = ImageListSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=ExpertImage.objects.all()



class ExpertUserProfileAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertProfile
    def get_queryset(self):
        user=BaseUser.objects.get(id=self.kwargs.get("id"))
        return Expert.objects.filter(user=user)

class ExpertUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterExpertSerializer
    queryset = Expert.objects.all()



class OpeningHoursCreateApiView(ListCreateAPIView):
    permission_classes=[IsAuthenticated,IsExpert]
    serializer_class = CreateOpeningHoursSerializer
    queryset=OpeningHours.objects.all()



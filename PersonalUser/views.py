from rest_framework.permissions import AllowAny,IsAuthenticated
from PersonalUser.models import *
from .serializers import *
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import generics


class PersonalUserProfileAPIView(generics.ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerPersonalUserProfile
    def get_queryset(self):
        return PersonalAccount.objects.filter(user__id=self.kwargs.get("customer_id"))

class PersonalUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = PersonalAccount.objects.all()

class CallExpertCreateApiView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = PersonalUserCallExpertSerializer
    queryset=PersonalAccount.objects.all()

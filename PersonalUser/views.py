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
        user=BaseUser.objects.get(id=self.kwargs.get("customer_id"))
        return PersonalAccount.objects.filter(user=user)

class PersonalUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = PersonalAccount.objects.all()


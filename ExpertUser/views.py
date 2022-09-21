from rest_framework.permissions import AllowAny,IsAuthenticated
from ExpertUser.models import *
from .serializers import *
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import generics


class ExpertUserProfileAPIView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class   = SerializerExpertProfile
    def get_queryset(self):
        user=BaseUser.objects.get(id=self.kwargs.get("id"))
        return Expert.objects.get(user=user)

class ExpertUserRegisterAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = RegisterExpertSerializer
    queryset = Expert.objects.all()

from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView,ListAPIView
from GuestUser.serializers import GuestCallExpertSerializer
from GuestUser.models import GuestUser
from GuestUser.serializers import GuestSerializer

class CallExpertCreateApiView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = GuestCallExpertSerializer
    queryset=GuestUser.objects.all()


class GuestRegisterCreateApiView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = GuestSerializer
    queryset=GuestUser.objects.all()

class GetGuestInfoApiView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class = GuestSerializer
    def get_queryset(self):
        return GuestUser.objects.filter(id==self.kwargs.get("guestid"))

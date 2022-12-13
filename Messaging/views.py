from rest_framework.permissions import IsAuthenticated
from PersonalUser.models import *
from .serializers import *
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import CreateAPIView

class SendMessageAPIView(CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = SerializerSendMessage
    queryset = Message.objects.all()
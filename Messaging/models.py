from django.db import models
from BaseUser.models import BaseUser
from datetime import datetime    


class Message(models.Model):
     sender = models.ForeignKey(BaseUser, related_name="sender",on_delete=models.CASCADE)
     reciever = models.ForeignKey(BaseUser, related_name="reciever",on_delete=models.CASCADE)
     msg_content = models.TextField(verbose_name="Message Content")
     created_at =  models.DateTimeField(default=datetime.now,verbose_name="Mesaj Atılma Tarihi")
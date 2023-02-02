from time import timezone
from django.db import models
from BaseUser.models import *
from ExpertUser.models import Expert



class PersonalAccount(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True,related_name="customerprofile")
    favoriteexperts=models.ManyToManyField(Expert,related_name="favoriteexperts",verbose_name="Favori Çağrılar")
    previusexpertcalls=models.ManyToManyField(Expert,related_name="previusexperts",verbose_name="Önceki Çağrılar")
    password=models.TextField(verbose_name="Şifre")
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name        = "Customer"
        verbose_name_plural = "Customers"
        db_table            = "PersonalUsers"
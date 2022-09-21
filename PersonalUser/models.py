from time import timezone
from django.db import models
from BaseUser.models import *
from ExpertUser.models import Expert



class PersonalAccount(models.Model):

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    favoriteexperts=models.ManyToManyField(Expert)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name        = "Customer"
        verbose_name_plural = "Customers"
        db_table            = "PersonalUsers"
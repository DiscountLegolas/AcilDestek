from django.db import models
from django.utils.translation import gettext_lazy as _
from ExpertUser.models import Expert


class GuestUser(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6,default=1.0)
    lat  =  models.DecimalField(max_digits=9, decimal_places=6,default=1.0)
    previusexpertcalls=models.ManyToManyField(Expert,verbose_name="Önceki Çağrılar")


    class Meta:
        verbose_name        = "GuestUser"
        verbose_name_plural = "GuestUsers"
        db_table            = "GuestUsers"
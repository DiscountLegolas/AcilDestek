from django.db import models

class İl(models.Model):
    name=models.CharField(max_length=15)
    class Meta:
        verbose_name        = "City"
        verbose_name_plural = "Cities"
        db_table            = "Cities"

class İlçe(models.Model):
    name=models.CharField(max_length=15)
    il = models.ForeignKey(İl, on_delete=models.CASCADE)
    class Meta:
        verbose_name        = "District"
        verbose_name_plural = "Districts"
        db_table            = "Districts"

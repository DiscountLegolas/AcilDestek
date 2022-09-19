from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class ServiceCategory(MPTTModel):

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"
        db_table="Categories"
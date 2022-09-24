from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class ServiceCategory(models.Model):

    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"
        db_table="Categories"
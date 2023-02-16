from unicodedata import name
from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name='nested_category', on_delete=models.CASCADE)

    def subcategories(self):
        return ServiceCategory.objects.filter(parent=self)
        
    def expertcount(self):
        return self.experts.count()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"
        db_table="Categories"
from django.db import models
from BaseUser.models import *
from ExpertUser.models import *


class Employee(models.Model):

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True,related_name="emloyeeprofile")
    employer=models.ForeignKey(Expert, on_delete=models.SET_NULL,null=True,related_name="employees")

    class Meta:
        verbose_name        = "Employee"
        verbose_name_plural = "Employees"
        db_table            = "Employees"

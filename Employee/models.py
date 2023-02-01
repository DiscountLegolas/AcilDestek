from django.db import models
from BaseUser.models import *
from ExpertUser.models import *


class Employee(models.Model):

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True,related_name="emloyeeprofile")
    employer=models.ForeignKey(Expert, on_delete=models.SET_NULL,null=True,related_name="employees")
    password=models.TextField(verbose_name="Şifre",default="pbkdf2_sha256$390000$aFPItBeusjwW6y5YrbOSwY$bpQAkv4VVQBG5W+bc3pK2ybUHvmBBXvso7odOh5p4Sg=")

    class Meta:
        verbose_name        = "Employee"
        verbose_name_plural = "Employees"
        db_table            = "Employees"

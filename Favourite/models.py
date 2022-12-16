from django.db import models
from BaseUser.models import BaseUser
from ExpertUser.models import Expert
# Create your models here.

class UserFavExpert(models.Model):
    user = models.ForeignKey(BaseUser,on_delete=models.CASCADE,default=1)
    expert = models.ForeignKey(Expert,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name_plural = 'User favourite experts'

    def __str__(self):
        return self.user.first_name 
    
from django.db import models
from BaseUser.models import BaseUser
from ExpertUser.models import Expert
from GuestUser.models import GuestUser

# Create your models here.

class UserFavExpert(models.Model):
    user = models.ForeignKey(BaseUser,on_delete=models.CASCADE,default=1,related_name="favorites")
    expert = models.ForeignKey(Expert,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name_plural = 'User favourite experts'

    def __str__(self):
        return self.user.email 


class GuestUserFavExpert(models.Model):
    user = models.ForeignKey(GuestUser,on_delete=models.CASCADE,default=1,related_name="favorites")
    expert = models.ForeignKey(Expert,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name_plural = 'User favourite experts'

    def __str__(self):
        return self.user.email 
    
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.core.validators import MaxValueValidator, MinValueValidator
from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from datetime import datetime    


class ExpertReview(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name="puanlama")
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE,verbose_name="Yorum Yapılan Usta",related_name="Expert")
    text = models.CharField(max_length=200,default="SomeText",verbose_name="Yorum Yazısı")
    user = models.ForeignKey(PersonalAccount, on_delete=models.SET_NULL,null=True,verbose_name="Yorumu Atan Müşteri")
    createdDate = models.DateTimeField(default=datetime.now,verbose_name="Oluşturulma Tarihi")
    isAnonymous=models.BooleanField(default=False)

    @property
    def customernamesurname(self):
        if self.isAnonymous:
            return None
        else:
            return self.user.user.first_name+" "+self.user.user.last_name


    def __str__(self):
        return  self.text 
    
    class Meta:
        constraints = [
            CheckConstraint(check=Q(rate__range=(0, 5)), name='valid_rate'),
        ]
        verbose_name        = "Review"
        verbose_name_plural = "Reviews"
        db_table="Reviews"

from unicodedata import decimal
from django.db import models
import uuid
from BaseUser.models import *
from django.db.models import Sum
from django.apps import apps
from django.utils.translation import gettext_lazy as _

WEEKDAYS = [
    (1, _("Pazartesi")),
    (2, _("Salı")),
    (3, _("Çarşamba")),
    (4, _("Perşembe")),
    (5, _("Cuma")),
    (6, _("Cumartesi")),
    (7, _("Pazar")),
]




class Expert(models.Model):

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True)
    description=models.TextField(verbose_name="Açıklama",null=True)
    companyname=models.CharField(max_length=50,verbose_name="İşyeri İsmi",null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6,default=1.0)
    lat  =  models.DecimalField(max_digits=9, decimal_places=6,default=1.0)
    category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE,verbose_name="Kategorisi")


    @property
    def averagescore(self):
        ExpertReview = apps.get_model(app_label='Comment', model_name='ExpertReview')
        reviewcount= decimal(ExpertReview.objects.filter(expert=self).count())
        sumofratings=ExpertReview.objects.filter(expert=self).aggregate(Sum('rate'))
        return sumofratings/reviewcount
    
    @property
    def countofreviews(self):
        ExpertReview = apps.get_model(app_label='Comment', model_name='ExpertReview')
        reviewcount= decimal(ExpertReview.objects.filter(expert=self).count())
        return reviewcount
    
    @property
    def workinghours(self):
        openings=OpeningHours.objects.filter(company=self)
        return openings
    
    @property
    def expertimages(self):
        images=ExpertImage.objects.filter(expert=self)
        return images
    

    def __str__(self):
        return self.user.email+self.companyname
    
    class Meta:
        verbose_name        = "Expert"
        verbose_name_plural = "Experts"
        db_table="Experts"



class OpeningHours(models.Model):

    class Meta:
        verbose_name = _('Working time')  # plurale tantum
        verbose_name_plural = _('Working times')
        ordering = [ 'weekday', 'from_hour']

    company = models.ForeignKey(Expert,on_delete=models.CASCADE, verbose_name=_('Company'))
    weekday = models.IntegerField(_('Weekday'), choices=WEEKDAYS)
    is_closed=models.BooleanField(default=True)
    from_hour = models.TimeField(_('Opening'))
    to_hour = models.TimeField(_('Closing'))

    def __str__(self):
        return _("%(company)s - %(weekday)s  %(from_hour)s - %(to_hour)s") % {
            'company':self.company.companyname,
            'weekday': self.get_weekday_display(),
            'from_hour': self.from_hour,
            'to_hour': self.to_hour
        }


class ExpertImage(models.Model):
    id = models.UUIDField( primary_key = True,default = uuid.uuid4,editable = False)
    expert = models.ForeignKey(Expert,on_delete=models.CASCADE,verbose_name="Expert")
    image = models.ImageField(upload_to="images",verbose_name="Expert Image")

    def __str__(self):
        return self.expert.companyname + self.id

    class Meta:
        verbose_name = "Expert Image"
        verbose_name_plural = "Expert Images"
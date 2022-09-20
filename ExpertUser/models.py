from unicodedata import decimal
from django.db import models
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
    is_closed=models.BooleanField(default=True)

<<<<<<< HEAD
    def __str__(self):
        return _("%(company)s - %(weekday)s  %(from_hour)s - %(to_hour)s") % {
=======
    def str(self):
        return _(" %(company)s - %(weekday)s  %(from_hour)s - %(to_hour)s") % {
>>>>>>> 00586e609e34c33e74f07fb0a99ad004ffe29811
            'company':self.company.companyname,
            'weekday': self.get_weekday_display(),
            'from_hour': self.from_hour,
            'to_hour': self.to_hour
        }
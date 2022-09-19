from django.db import models

from time import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from Category.models import ServiceCategory
from django.utils.encoding import force_bytes
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  
from django.utils.http import urlsafe_base64_encode  
from django.template.loader import render_to_string  
from Location.models import *
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class BaseUser(AbstractUser):
    phone_message = 'Telefon numarası 05999999999 formatında olmalıdır' 
    phone_regex = RegexValidator(
        regex=r'^(05)\d{9}$',
        message=phone_message
    )
    email = models.EmailField(_('email address'), unique=True)
    username=None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    def how_many_days(self):
        return (timezone.now()-self.date_joined).days
    def name_surname(self):
        return self.first_name+self.last_name


    def sendactivationmail(self,current_site):
        user=self
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('acc_active_email.html', {  
            'user': user,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            'token':account_activation_token.make_token(user),  
        })  
        to_email = self.email
        email = EmailMessage(  
                mail_subject, message, to=[to_email]  
        )  
        email.send()  

    phone = models.CharField(validators=[phone_regex], max_length=60,null=True, blank=True)
    il=models.ForeignKey(İl,on_delete=models.SET_NULL,null=True)
    ilçe=models.ForeignKey(İlçe,on_delete=models.SET_NULL,null=True)
    is_expert = models.BooleanField(default=False)
    is_regular = models.BooleanField(default=False)

    
    class Meta:
        verbose_name        = "BaseUser"
        verbose_name_plural = "BaseUsers"
        db_table            = "BaseUsers"

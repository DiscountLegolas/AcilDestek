"""acildestek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.exceptions import AuthenticationFailed
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from BaseUser.models import BaseUser 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ExpertUser.models import Expert
from PersonalUser.models import PersonalAccount
from Employee.models import Employee
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import  get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User=get_user_model()
class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class CustomJWTSerializer(TokenObtainPairSerializer):

    username_field = 'email_or_phone'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField()
        self.fields['usertype']=serializers.IntegerField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
            'usertype':attrs['usertype']
        }
        default_error_messages = {
            'no_active_account': _('No active account found with the given credentials'),
            'expertaccountfalse': _('e-mail or password invalid for ExpertUser'),
            'personalaccountfalse': _('e-mail or password invalid for PersonalAccount'),
            'employeeaccountfalse': _('e-mail or password invalid for EmployeeAccount')
        }
        user_obj = User.objects.filter(email=attrs.get("email_or_phone")).first() or User.objects.filter(phone=attrs.get("email_or_phone")).first()
        if user_obj:
            match int(attrs.get("usertype")):
                case 1:
                    user_obj.role=BaseUser.EXPERT
                    if check_password(attrs.get("password"), Expert.objects.get(user=user_obj).password)==False:
                        raise AuthenticationFailed(
                        self.error_messages['expertaccountfalse'],
                            'expertaccountfalse',)
                case 2:
                    user_obj.role=BaseUser.CUSTOMER
                    if check_password(attrs.get("password"), PersonalAccount.objects.get(user=user_obj).password)==False:
                        raise AuthenticationFailed(
                        self.error_messages['personalaccountfalse'],
                            'personalaccountfalse',)
                case 3:
                    user_obj.role=BaseUser.EMPLOYEE
                    if check_password(attrs.get("password"), PersonalAccount.objects.get(user=user_obj).password)==False:
                        raise AuthenticationFailed(
                        self.error_messages['employeeaccountfalse'],
                            'employeeaccountfalse',)
                case default:
                    return "something"
                            
            user_obj.save()
            refresh = RefreshToken.for_user(user_obj)
            refresh['usertype'] = int(attrs.get("usertype"))
            return {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                }
            
        else:
            raise AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',)



schema_view = get_schema_view(
   openapi.Info(
      title="AcilDestek API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 
        include([
            path('user/', include("BaseUser.urls", namespace="baseuser"), name="url_user"),
            path('category/', include("Category.urls", namespace="baseuser"), name="url_user"),
            path('personaluser/', include("PersonalUser.urls", namespace="personaluser"), name="url_personaluser"),
            path('expert/', include("ExpertUser.urls", namespace="expertuser"), name="url_expertuser"),
            path('employee/', include("Employee.urls", namespace="employee"), name="url_employee"),
            path('comment/', include("Comment.urls", namespace="comment"), name="url_comment"),
            path('guest/', include("GuestUser.urls", namespace="guest"), name="url_guest"),
            path('favourite/',include("Favourite.urls",namespace="quest"),name="url_favourite"),
            path('message/', include("Messaging.urls", namespace="message"), name="url_message"),
            path('token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer)),
            path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
        ])
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
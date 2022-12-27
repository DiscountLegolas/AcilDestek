from django.urls import path,re_path
from .views import *

app_name="baseuser"
urlpatterns = [
        path('activate/<uidb64>/<token>/',activate, name='activate'),
        path("callexpert/",CallExpertCreateApiView.as_view(),name="url_callexpert"),
        path("accounttypes/",AccountTypesView.as_view(),name="url_callexpert"),
        re_path(r'^expertsnear/$',GetGoodExpertsNearMeAPIView.as_view(),name="url_callexpert"),
        re_path(r'^search/$',SearchAPIView.as_view(),name="url_search"),
        path("profiles",ProfileGetAPIView.as_view(),name="profile",),
        path("Otp/",PasswordReset.as_view(),name="get_otp",),
        path("OtpValidate/",VerifyOtp.as_view(),name="validate_otp",),
        path("password-reset/<str:email>/",ResetPasswordAPI.as_view(),name="reset-password",),
]

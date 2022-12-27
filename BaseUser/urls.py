from django.urls import path,re_path
from .views import *

app_name="baseuser"
urlpatterns = [
        path('activate/<uidb64>/<token>/',activate, name='activate'),
        path("callexpert/",CallExpertCreateApiView.as_view(),name="url_callexpert"),
        path("accounttypes/",AccountTypesView.as_view(),name="url_callexpert"),
        re_path(r'^expertsnear/$',GetGoodExpertsNearMeAPIView.as_view(),name="url_callexpert"),
        re_path(r'^search/$',SearchAPIView.as_view(),name="url_search"),
        path("",PasswordReset.as_view(),name="request-password-reset",),
        path("profiles",ProfileGetAPIView.as_view(),name="profile",),
        path("password-reset/",PasswordReset.as_view(),name="reset-password",),
        path("password-reset/<str:encoded_pk>/<str:token>/",ResetPasswordAPI.as_view(),name="reset-password_reset",),
]

from django.urls import path,re_path
from .views import *

app_name="baseuser"
urlpatterns = [
        path('activate/<uidb64>/<token>/',activate, name='activate'),
        path("callexpert/",CallExpertCreateApiView.as_view(),name="url_callexpert"),
        re_path(r'^expertsnear/$',GetGoodExpertsNearMeAPIView.as_view(),name="url_callexpert"),

]

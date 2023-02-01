from django.urls import path
from .views import ExpertUserProfileAPIView,ExpertUserRegisterAPIView,OpeningHoursUpdateApiView,UploadExpertPhoto
from PersonalUser import views
from rest_framework.routers import DefaultRouter
openinghoursupdate = OpeningHoursUpdateApiView.as_view({
    'post': 'create',
})
uploadphotos = UploadExpertPhoto.as_view({
    'post': 'create',
})
app_name="expertuser"
urlpatterns = [
    path("register/",ExpertUserRegisterAPIView.as_view(),name="url_register"),
    path("profile/<int:id>",ExpertUserProfileAPIView.as_view(),name="url_expert_profile"),
    path("profile/updatehours/",openinghoursupdate),   
    path("profile/uploadphotos/",uploadphotos),
]

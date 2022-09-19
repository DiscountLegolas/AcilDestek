from django.urls import path
from .views import activate

app_name="baseuser"
urlpatterns = [
        path('activate/<uidb64>/<token>/',activate, name='activate'),
]

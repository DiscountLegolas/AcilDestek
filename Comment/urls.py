from django.urls import path
from .views import ExpertReviewListByExpertAPIView,CreateExpertReviewAPIView
from PersonalUser import views

app_name="comment"
urlpatterns = [
    path("list/<int:expert_id>",ExpertReviewListByExpertAPIView.as_view(),name="url_commentlist"),
    path("create/<int:expert_id>",CreateExpertReviewAPIView.as_view(),name="url_commentcreate")
]

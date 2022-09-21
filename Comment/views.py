from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from Comment.models import ExpertReview
from ExpertUser.models import Expert
from BaseUser.permissions import IsCustomer
from .serializers import SerializerExpertReviewListByExpert,SerializerCreateExpertReview
from rest_framework.permissions import IsAuthenticated,AllowAny
from .pagination import ExpertReviewPagination


class ExpertReviewListByExpertAPIView(ListAPIView):
    serializer_class   = SerializerExpertReviewListByExpert
    permission_classes = [AllowAny]
    pagination_class   = ExpertReviewPagination

    def get_queryset(self):
        return ExpertReview.objects.filter(expert__user__id=self.kwargs.get("expert_id")).order_by("-createdDate")


class CreateExpertReviewAPIView(CreateAPIView):
    queryset           = ExpertReview.objects.all()
    serializer_class   = SerializerCreateExpertReview
    permission_classes = [IsAuthenticated,IsCustomer]

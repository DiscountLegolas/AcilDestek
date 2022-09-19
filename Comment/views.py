from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from Comment.models import ExpertReview
from ExpertUser.models import Expert
from .serializers import SerializerDeleteExpertReview, SerializerExpertReviewListByExpert,SerializerCreateExpertReview
from rest_framework.permissions import IsAuthenticated
from .pagination import ExpertReviewPagination


class ExpertReviewListByExpertAPIView(ListAPIView):
    serializer_class   = SerializerExpertReviewListByExpert
    permission_classes = [IsAuthenticated]
    pagination_class   = ExpertReviewPagination

    def get_queryset(self):
        return ExpertReview.objects.filter(expert__user__id=self.kwargs.get("expert_id")).order_by("-createdDate")


class CreateExpertReviewAPIView(CreateAPIView):
    queryset           = ExpertReview.objects.all()
    serializer_class   = SerializerCreateExpertReview
    permission_classes = [IsAuthenticated]

'''
class DeleteExpertReviewAPIView(DestroyAPIView):
   queryset           = ExpertReview.objects.all()
   lookup_field       = "id"
    permission_classes = [IsAuthenticated,IsOwner]    serializer_class   = SerializerDeleteExpertReview

    def perform_destroy(self, instance):
        instance.delete()
'''
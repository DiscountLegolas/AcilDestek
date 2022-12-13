import decimal
from django.http import HttpResponse  
from django.utils.http import  urlsafe_base64_decode
from rest_framework.generics import CreateAPIView,ListAPIView
from BaseUser.serializers import CallExpertSerializer
from ExpertUser.serializers import SerializerExpertSimpleInfo
from GuestUser.models import GuestUser
from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from Category.models import ServiceCategory    
from .tokens import account_activation_token 
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .tokens import account_activation_token 
from django.contrib.postgres.search import TrigramSimilarity 
from django.utils.encoding import force_str

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')


class CallExpertCreateApiView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = CallExpertSerializer
    def get_queryset(self):
        if self.request.user!=None and self.request.user.is_customer==True:
            return PersonalAccount.objects.all()
        else:
            return GuestUser.objects.all()


class GetGoodExpertsNearMeAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertSimpleInfo

    def get_queryset(self):
        cats=self.request.GET.getlist("categories",'')
        categories=ServiceCategory.objects.all()
        if cats is not '':
            categories=ServiceCategory.objects.filter(name__in=cats)
        long=decimal.Decimal(self.request.GET.get("long")) 
        lat=decimal.Decimal(self.request.GET.get("lat"))
        if self.request.user.is_anonymous:
            sorted_results = sorted(Expert.objects.filter(categories__in=categories), key= lambda t: (t.distancetopoint(long=long,lat=lat),t.averagescore))
            sorted_results=sorted_results[:10]
            return sorted_results
        elif self.request.user.is_regular:
            qs = Expert.objects.filter(user__il=self.request.user.il,user__ilçe=self.request.user.ilçe,categories__in=categories)
            unsorted_results = qs.all()
            sorted_results = sorted(unsorted_results, key= lambda t: (t.distancetopoint(long=long,lat=lat),t.averagescore))
            sorted_results=sorted_results[:10]
            return sorted_results

class SearchAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertSimpleInfo

    def get_queryset(self):
        q=self.request.GET.get('q','')
        results = Expert.objects.filter(companyname__trigram_similar=q).annotate(similar=TrigramSimilarity('companyname',q)).filter(similarity__gt=0.01).order_by('-similar')
        return results
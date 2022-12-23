import decimal
from django.http import HttpResponse  
from django.utils.http import  urlsafe_base64_decode
from rest_framework.generics import CreateAPIView,ListAPIView,GenericAPIView
from BaseUser.serializers import CallExpertSerializer,AccountTypesSerializer
from ExpertUser.serializers import SerializerExpertSimpleInfo
from GuestUser.models import GuestUser
from rest_framework.response import Response

from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from Category.models import ServiceCategory    
from BaseUser.models import BaseUser    
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

class AccountTypesView(GenericAPIView):
    permission_classes=[AllowAny]
    def get(self, request):
        emailistaken=True if BaseUser.objects.filter(email=self.request.GET.get("email")).exists() else False
        if BaseUser.objects.filter(email=self.request.GET.get("email")).exists()==False:
            emailistaken=False
            expertprofileexists=False
            customerprofileexists=False
            employeeprofileexists=False
            datatoserialize={"emailistaken":emailistaken,"expertprofileexists":expertprofileexists,"customerprofileexists":customerprofileexists,"employeeprofileexists":employeeprofileexists}
            serializer = AccountTypesSerializer(datatoserialize)
            return Response(serializer.data)
        else:
            emailistaken=True
            user=BaseUser.objects.filter(email=self.request.GET.get("email")).first()
            datatoserialize={"emailistaken":emailistaken,"expertprofileexists":user.is_expert,"customerprofileexists":user.is_regular,"employeeprofileexists":user.is_employee}
            serializer = AccountTypesSerializer(datatoserialize)
            return Response(serializer.data)

class GetGoodExpertsNearMeAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertSimpleInfo

    def get_queryset(self):
        cats=self.request.GET.getlist("categories",'')
        categories=ServiceCategory.objects.all()
        if cats != '':
            categories=ServiceCategory.objects.filter(name__in=cats)
        long=decimal.Decimal(self.request.GET.get("long")) 
        lat=decimal.Decimal(self.request.GET.get("lat"))
        if self.request.user.is_anonymous:
            sorted_results = sorted(Expert.objects.filter(category__in=categories), key= lambda t: (t.distancetopoint(long=long,lat=lat),t.averagescore))
            sorted_results=sorted_results[:10]
            return sorted_results
        elif self.request.user.is_regular:
            qs = Expert.objects.filter(user__il=self.request.user.il,user__ilçe=self.request.user.ilçe,category__in=categories)
            unsorted_results = qs.all()
            sorted_results = sorted(unsorted_results, key= lambda t: (t.distancetopoint(long=long,lat=lat),t.averagescore))
            sorted_results=sorted_results[:10]
            return sorted_results

class SearchAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class   = SerializerExpertSimpleInfo

    def get_queryset(self):
        q=self.request.GET.get('q','')
        cats=self.request.GET.getlist("categories",'')
        categories=ServiceCategory.objects.all()
        if cats != '':
            categories=ServiceCategory.objects.filter(name__in=cats)
        results = Expert.objects.filter(category__in=categories,companyname__icontains=q)
        return results
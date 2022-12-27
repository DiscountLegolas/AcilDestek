from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import cache_page
import decimal
import random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string  
from django.utils.decorators import method_decorator
from rest_framework import generics, status, response
from django.http import HttpResponse  
from django.utils.http import  urlsafe_base64_decode,urlsafe_base64_encode
from rest_framework.generics import CreateAPIView,ListAPIView,GenericAPIView
from BaseUser.serializers import CallExpertSerializer,AccountTypesSerializer,EmailSerializer,ResetPasswordSerializer,ProfileSerializer,OtpEmailSerializer
from ExpertUser.serializers import SerializerExpertSimpleInfo,SerializerExpertSimpleInfoF
from GuestUser.models import GuestUser
from rest_framework.response import Response
from PersonalUser.models import PersonalAccount
from ExpertUser.models import Expert
from Category.models import ServiceCategory    
from BaseUser.models import BaseUser    
from .tokens import account_activation_token 
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import get_user_model
from .tokens import account_activation_token 
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
    serializers_classes=(SerializerExpertSimpleInfoF,SerializerExpertSimpleInfo)
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
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def list(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            self.serializer_class = self.serializers_classes[1]
            return super().list(request, *args, **kwargs)

        self.serializer_class = self.serializers_classes[0]
        return super().list(request, *args, **kwargs)

class SearchAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializers_classes=(SerializerExpertSimpleInfoF,SerializerExpertSimpleInfo)
    def get_queryset(self):
        q=self.request.GET.get('q','')
        cats=self.request.GET.getlist("categories",'')
        categories=ServiceCategory.objects.all()
        if cats != '':
            categories=ServiceCategory.objects.filter(name__in=cats)
        results = Expert.objects.filter(category__in=categories,companyname__icontains=q)
        return results

    def list(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            self.serializer_class = self.serializers_classes[1]
            return super().list(request, *args, **kwargs)

        self.serializer_class = self.serializers_classes[0]
        return super().list(request, *args, **kwargs)



class ProfileGetAPIView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ProfileSerializer

    
    def list(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class PasswordReset(generics.GenericAPIView):

    serializer_class = EmailSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = BaseUser.objects.filter(email=email).first()
        if user:
            number_list = [x for x in range(10)]  # Use of list comprehension
            code_items_for_otp = []
            for i in range(6):
                num = random.choice(number_list)
                code_items_for_otp.append(num)

            code_string = "".join(str(item) for item in code_items_for_otp)
            user.otp=code_string
            user.save()
            mail_subject = 'Reset Password Code has been sent to your email id'  
            message = render_to_string('password_reset.html', {  
            'user': user,
            'resetcode':code_string
            })  
            to_email = user.email
            email = EmailMessage(  
                mail_subject, message, to=[to_email]  
            )  
            email.send()  

            return response.Response(
                {
                    "message": 
                    f"Your Code: Has Been Sent"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class VerifyOtp(generics.GenericAPIView):

    serializer_class = OtpEmailSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        iscorrect = BaseUser.objects.filter(email=email,otp=serializer.data["otp"]).exists()

        return response.Response(
            {
                "otpcorrect":iscorrect
            },
            status=status.HTTP_200_OK,
        )


class ResetPasswordAPI(generics.GenericAPIView):

    serializer_class = ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
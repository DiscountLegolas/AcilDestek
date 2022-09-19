from django.http import HttpResponse  
from django.utils.http import  urlsafe_base64_decode    
from .tokens import account_activation_token  
from django.contrib.auth import get_user_model
import django
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
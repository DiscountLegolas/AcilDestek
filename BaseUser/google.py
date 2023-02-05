from google.auth.transport import requests
import os
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed,NotFound
from django.contrib.auth import authenticate
from BaseUser.models import BaseUser
from acildestek.urls import CustomJWTSerializer


class Google:
    """Google class to fetch the user info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the user info
        """
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request())

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo

        except:
            return "The token is either invalid or has expired"


def social_user(provider, user_id, email, name):
    filtered_user_by_email = BaseUser.objects.filter(email=email).first()

    if filtered_user_by_email.exists():
        userype="expert" if bool(filtered_user_by_email.expert()) else "customer" if bool(filtered_user_by_email.customer()) else "employee" 
        return {
            'email': filtered_user_by_email.email,
            'usertype':userype
        }

    else:
        raise NotFound(detail="User Not Exists")

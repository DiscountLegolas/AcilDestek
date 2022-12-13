from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Expert

class GetProfilePuppiesTestCase(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = "/profile/<int:id>"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

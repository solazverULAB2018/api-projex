from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework import status
from api.models import Project
import json

class APIWrapperClass(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()    
        url = '/api/v1/api-token-auth/'
        response = self.client.post(url, {'username_or_email':'pepe@pepe.com', 'password':'12345678ju'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

import json

from glob import glob
from io import StringIO
from unittest.mock import patch

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory,APITestCase

from users.models import CustomUser


class UserRegistrationAPIViewTestCase(APITestCase):
    #url = reverse("users:list")
    url = '/api/v1/rest-auth/registration/'
    avatar = glob('*png')

    def setUp(self):
        print(self.avatar)

    def test_invalid_password1(self):
        """
        Test to verify that a post call with invalid(unmatch) passwords
        """
        data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "password",
            "password2": "INVALID_PASSWORD",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)

    def test_invalid_password2(self):
        """
        Test to verify that a post call with invalid(short) passwords
        """
        data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "1234567",
            "password2": "1234567",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)

    def test_invalid_password3(self):
        """
        Test to verify that a post call with invalid(simple) passwords
        """
        data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "12345678",
            "password2": "12345678",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "123aT678",
            "password2": "123aT678",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    #@patch('django.core.files.storage.FileSystemStorage.save')
    def test_user_registration_with_photo(self):#, mock_save):
        """
        Test to verify that a post call with user valid data with photo
        """
        #mock_save.return_value = 'photo.jpg'
        data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "123aT678",
            "password2": "123aT678",
            "country": "Venezuela",
            #"profile_photo": StringIO('test'),
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    def test_unique_username_validation(self):
        """
        Test to verify that a post call with already exists username
        """
        user1 = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "123aT678",
            "password2": "123aT678",
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user1)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        user2 = {
            "username": "testuser",
            "email": "test2@testuser.com",
            "password1": "123aT678",
            "password2": "123aT678",
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user2)
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)

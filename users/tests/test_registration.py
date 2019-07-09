import json

from io import StringIO
from unittest.mock import patch

from rest_framework.test import APITestCase


class UserRegistrationAPIViewTestCase(APITestCase):
    url = '/api/v1/rest-auth/registration/'
    username = "testuser"
    email = "test@testuser.com"
    password = "12345Hola"

    def setUp(self):
        pass

    def test_invalid_password_unmatch(self):
        """
        Test to verify that a post call with invalid(unmatch) passwords
        """
        data = {
            "username": self.username,
            "email":    self.email,
            "password1": "passwordStrong",
            "password2": "INVALID_PASSWORD",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue("password1" in json.loads(response.content))

    def test_invalid_password_short(self):
        """
        Test to verify that a post call with invalid(short) passwords
        """
        data = {
            "username": self.username,
            "email":    self.email,
            "password1": "123Hola",
            "password2": "123Hola",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue("password1" in json.loads(response.content))

    def test_invalid_password_simple(self):
        """
        Test to verify that a post call with invalid(simple) passwords
        """
        data = {
            "username": self.username,
            "email":    self.email,
            "password1": "12345678",
            "password2": "12345678",
            "country": "Venezuela",
            #"profile_photo": "",
        }
        response = self.client.post(self.url, data, format='json')
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue("password1" in json.loads(response.content))

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        data = {
            "username":  self.username,
            "email":     self.email,
            "password1": self.password,
            "password2": self.password,
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
            "username":  self.username,
            "email":     self.email,
            "password1": self.password,
            "password2": self.password,
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
            "username":  self.username,
            "email":     self.email,
            "password1": self.password,
            "password2": self.password,
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user1)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        user2 = {
            "username":  self.username,
            "email": "test2@testuser.com",
            "password1": self.password,
            "password2": self.password,
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user2)
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue("username" in json.loads(response.content))

    def test_unique_email_validation(self):
        """
        Test to verify that a post call with already exists email
        """
        user1 = {
            "username":  self.username,
            "email":     self.email,
            "password1": self.password,
            "password2": self.password,
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user1)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        user2 = {
            "username":  'testuser2',
            "email":     self.email,
            "password1": self.password,
            "password2": self.password,
            "country": "Venezuela",
        }
        response = self.client.post(self.url, user2)
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue("email" in json.loads(response.content))

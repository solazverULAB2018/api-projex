import json

from io import StringIO
from unittest.mock import patch

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase

from users.models import CustomUser


class UserLoginAPIViewTestCase(APITestCase):
    #url = reverse("users:list")
    url = '/api/v1/rest-auth/%s/'
    username = "testuser"
    email = "test@testuser.com"
    password = "12345Hola"

    def setUp(self):
        self.user = CustomUser.objects.create_user(self.username, self.email, self.password)

    def test_authentication_with_valid_data(self):
        """
        Test to verify a login post call with user valid data
        """
        data = {
            "username": self.username,
            "email":    self.email,
            "password": self.password,
        }
        response = self.client.post(self.url%'login', data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    def test_authentication_with_valid_username(self):
        """
        Test to verify a token post call with just username
        """
        data = {
            "username": self.username,
            "password": self.password,
        }
        response = self.client.post(self.url%'login', data)
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_email(self):
        """
        Test to verify a token post call with just email
        """
        data = {
            "email":    self.email,
            "password": self.password,
        }
        response = self.client.post(self.url%'login', data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    def test_login_logout(self):
        """
        Test to verify a login and logout
        """
        data = {
            "email":    self.email,
            "password": self.password,
        }
        response = self.client.post(self.url%'login', data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

        response = self.client.get(self.url%'logout')
        self.assertEqual(200, response.status_code)
        self.assertTrue("detail" in json.loads(response.content))

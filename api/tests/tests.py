import json

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from users.models import CustomUser

from api.models import *
from api.serializers import *


class AuthBaseTestCase(APITestCase):
    email = "@testuser.com"
    password = "12345Hola"

    def setUp(self):
        self.user = CustomUser.objects.create_user('user', 'user'+self.email, self.password)
        self.jefe = CustomUser.objects.create_user('jefe', 'jefe'+self.email, self.password)
        self.emp1 = CustomUser.objects.create_user('emp1', 'emp1'+self.email, self.password)
        self.emp2 = CustomUser.objects.create_user('emp2', 'emp2'+self.email, self.password)
        self.api_authentication()

    def api_authentication(self):
        data = {
          "email":'jefe'+self.email,
          "password": self.password,
        }
        url = '/rest-auth/login/'
        response = self.client.post(url, data)
        print(response.status_code, response.content)


class ProjectTestCase(AuthBaseTestCase):
    url = '/api/v1/projects'

    def test_create_project_get(self):
        """
        Test to verify a valid GET project (Model and Serializer)
        """
        data = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
        }
        project = Project.objects.create(**data)
        pSerial = ProjectSerializer(instance=project)
        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)['results'][0]
        self.assertEqual(pSerial.data, response_data)

    def test_create_project_post(self):
        """
        Test to verify a valid POST project HTTP json
        """
        data = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe.id,
        }
        response = self.client.post(self.url, data)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

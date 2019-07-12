import json

from rest_framework.test import APITestCase

from users.models import CustomUser

from api.models import *
from api.serializers import *

from .authBase import AuthBaseTestCase



class ProjectTestCase(AuthBaseTestCase):
    url = '/api/v1/memberships'

    def setUp(self):
        super().setUp() # Create 4 users(user,jefe,emp1,emp2) and Login jefe
        self.client.logout() # Logout jefe
        self.client.login(username='emp1', password=self.password)
        self.data_project = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
          # "project_to_user": [
          #   self.emp1,
          #   self.emp2
          # ]
        }
        self.project = Project.objects.create(**self.data_project)
        self.data_project['creator'] = self.jefe.id
        self.data = {
          "user": self.emp1,
          "project": self.project,
          "role": "Backend",
          "status": "active",
        }
        self.emp1Proj = UserProject.objects.create(**self.data)


    def test_read_membership_get(self):
        """
        Test to verify GET membership valid (Model and Serializer)
        """
        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)['results']
        print(response_data)
        emp1ProjSerial = UserProjectSerializer(instance=self.emp1Proj)
        print(emp1ProjSerial.data)
        self.assertEqual(emp1ProjSerial.data, response_data[0])


    def test_create_membership_post(self):
        """
        Test to verify POST membership valid 
        """
        self.data['project'] = self.project.id
        self.data['user'] = self.emp2.id
        self.data['role'] = 'Frontend'

        response = self.client.post(self.url, self.data)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        self.client.logout() # Logout emp1
        self.client.login(username='emp2', password=self.password)
        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)['results']
        print(response_data)
        emp2Proj = UserProject.objects.get(user=self.emp2.id)
        emp2ProjSerial = UserProjectSerializer(instance=emp2Proj)
        print(emp2ProjSerial.data)
        self.assertEqual(emp2ProjSerial.data, response_data[0])

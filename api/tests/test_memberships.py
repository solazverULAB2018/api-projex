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


    def test_read_membership_get(self):
        """
        Test to verify GET membership valid (Model and Serializer)
        """
        data = self.data.copy()
        emp1Proj = UserProject.objects.create(**data)
        data['user'] = self.emp2
        data['role'] = 'Frontend'
        emp2Proj = UserProject.objects.create(**data)

        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)['results']
        print(response_data)
        emp1ProjSerial = UserProjectSerializer(instance=emp1Proj)
        print(emp1ProjSerial.data)
        self.assertEqual(emp1ProjSerial.data, response_data[0])

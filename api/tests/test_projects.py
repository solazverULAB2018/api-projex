import json

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
        self.client.login(username='jefe', password=self.password)



class ProjectTestCase(AuthBaseTestCase):
    url = '/api/v1/projects'

    def setUp(self):
        super().setUp() # Authenticanting
        self.data = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
        }
        self.project = Project.objects.create(**self.data)
        self.data['creator'] = self.jefe.id


    def test_read_project_get(self):
        """
        Test to verify GET project valid (Model and Serializer)
        """
        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)['results']
        project = Project.objects.get(title="black mesa")
        projectSerial = ProjectSerializer(instance=project)
        self.assertEqual(projectSerial.data, response_data[0])


    def test_read_project_get_by_another_user(self):
        """
        Test to verify GET project by a different user
        """
        self.client.logout()
        self.client.login(username='user', password=self.password)
        url = self.url+'/{id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        # the project doesn't belong to the user
        self.assertEqual(404, response.status_code) # Not found


    def test_create_project_post(self):
        """
        Test to verify POST project valid 
        """
        self.data['title'] = 'black mesa 2'
        response = self.client.post(self.url, self.data)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        response = self.client.get(self.url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        self.assertEqual(2, response_data['count']) # 2 projects


    def test_delete_project_delete(self):
        """
        Test to verify DELETE project valid
        """
        url = self.url+'/{id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.delete(url)
        print(response.status_code, response.content)
        self.assertEqual(204, response.status_code)
        self.assertEqual(b'', response.content)


    def test_update_project_patch(self):
        """
        Test to verify PATCH project valid 
        """
        data = {'title': 'Black Mesa.'}
        url = self.url+'/{id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.patch(url, data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertEqual(data['title'], response_data['title']) # updated


    def test_update_project_put(self):
        """
        Test to verify PUT project valid 
        """
        data = dict(self.data) # copy
        data['title'] = 'black mesa 1'
        url = self.url+'/{id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.put(url, data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertEqual(data['title'], response_data['title']) # updated


    def test_update_project_put_invalid_incomplete(self):
        """
        Test to verify PUT project invalid(incomplete)
        """
        data = {
          "title": "black mesa 1",
          "creator": self.jefe.id,
        }
        url = self.url+'/{id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.put(url, data)
        print(response.status_code, response.content)
        self.assertEqual(400, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertTrue("description" in response_data)


    def test_update_project_put_invalid_inexistent(self):
        """
        Test to verify PUT project invalid(inexistent) 
        """
        data = {
          "title": "black mesa 9",
          "description": "particle accelerator",
          "creator": self.jefe.id,
        }
        url = self.url+'/{id}'.format(id=self.project.id+9)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(404, response.status_code)

        response = self.client.put(url, data)
        print(response.status_code, response.content)
        self.assertEqual(404, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertTrue("detail" in response_data)

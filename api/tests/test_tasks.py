import json

from users.models import CustomUser

from api.models import *
from api.serializers import *

from .authBase import AuthBaseTestCase



class TaskTestCase(AuthBaseTestCase):
    url = '/api/v1/tasks'

    def setUp(self):
        super().setUp() # Create 4 users(user,jefe,emp1,emp2) and Login jefe
        self.data_project = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
        }
        self.project = Project.objects.create(**self.data_project)
        self.boards = Board.objects.filter(project=self.project.id)
        self.board = self.boards[0]
        print(self.boards)
        print(self.board)
        self.data = {
          "title": "task 1",
          "description": "first task",
          "priority": 1,
          "due_date": "2019-07-27",
          "board": self.board,
        }
        self.task = Task.objects.create(**self.data)
        self.data['board'] = self.board.id


    def test_read_task_get(self):
        """
        Test to verify GET task valid (Model and Serializer)
        """
        url = self.url + '?board={id}'.format(id=self.board.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        taskSerial = TaskSerializer(instance=self.task)
        print(taskSerial.data)
        self.assertEqual(taskSerial.data, response_data['results'][0])


    def test_create_task_post(self):
        """
        Test to verify POST task valid 
        """
        self.data['title'] = 'task 2'
        self.data['description'] = 'second task'
        self.data['board'] = self.board.id
        response = self.client.post(self.url, self.data)
        print(response.status_code, response.content)
        self.assertEqual(201, response.status_code)

        url = self.url + '?board={id}'.format(id=self.board.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        self.assertEqual(2, response_data['count']) # 2 projects


    def test_delete_task_delete(self):
        """
        Test to verify DELETE task valid
        """
        url = self.url+'/{task_id}?board={board_id}'.format(
                    task_id=self.task.id, board_id=self.board.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.delete(url)
        print(response.status_code, response.content)
        self.assertEqual(204, response.status_code)
        self.assertEqual(b'', response.content)


    def test_update_task_patch(self):
        """
        Test to verify PATCH task valid 
        """
        data = {'title': 'Task 1(one)'}
        url = self.url+'/{task_id}?board={board_id}'.format(
                    task_id=self.task.id, board_id=self.board.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.patch(url, data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertEqual(data['title'], response_data['title']) # updated


    def test_update_task_put(self):
        """
        Test to verify PUT task valid 
        """
        data = dict(self.data) # copy
        data['title'] = 'Task 1(one)'

        url = self.url+'/{task_id}?board={board_id}'.format(
                    task_id=self.task.id, board_id=self.board.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)

        response = self.client.put(url, data)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        self.assertEqual(data['title'], response_data['title']) # updated

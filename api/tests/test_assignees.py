import json

from users.models import CustomUser

from api.models import *
from api.serializers import *

from .authBase import AuthBaseTestCase



class BoardTestCase(AuthBaseTestCase):
    url = '/api/v1/assignees'

    def setUp(self):
        super().setUp() # Create 4 users(user,jefe,emp1,emp2) and Login jefe
        self.data_project = {
          "title": "black Mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
        }
        self.project = Project.objects.create(**self.data_project)
        self.boards = Board.objects.filter(project=self.project.id)
        self.board = self.boards[0]
        print(self.boards)
        print(self.board)
        self.data_task = {
          "title": "task 1",
          "description": "first task",
          "priority": 1,
          "due_date": "2019-07-27",
          "board": self.board,
        }
        self.task = Task.objects.create(**self.data_task)
        #self.data_task['board'] = self.board.id
        self.data_userProject = {
          "user": self.emp1,
          "project": self.project,
          "role": "Backend",
          "status": "active",
        }
        self.emp1Proj = UserProject.objects.create(**self.data_userProject)
        data = {
          "user": self.emp1,
          "task": self.task,
        }
        self.assigTask1_Emp1 = Assignee.objects.create(**data)


    def test_read_assignees_get(self):
        """
        Test to verify GET assignees valid (Model and Serializer)
        """
        url = self.url + '?task={id}'.format(id=self.task.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        assigneeSerial = AssigneeSerializer(instance=self.assigTask1_Emp1)
        print(assigneeSerial.data)
        self.assertEqual(assigneeSerial.data, response_data['results'][0])

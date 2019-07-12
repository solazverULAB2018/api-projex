import json

from users.models import CustomUser

from api.models import *
from api.serializers import *

from .authBase import AuthBaseTestCase



class BoardTestCase(AuthBaseTestCase):
    url = '/api/v1/comments'

    def setUp(self):
        super().setUp() # Create 4 users(user,jefe,emp1,emp2) and Login jefe
        self.data_project = {
          "title": "black mesa",
          "description": "particle accelerator",
          "creator": self.jefe,
        }
        self.project = Project.objects.create(**self.data_project)
        self.boards = Board.objects.all()
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
        self.data_task['board'] = self.board.id
        self.data = {
          "task": self.task,
          "creator": self.jefe,
          "text": "This task is very important",
        }
        self.comment = Comment.objects.create(**self.data)
        self.data['task'] = self.task.id
        self.data['jefe'] = self.jefe.id

    def test_read_comments_get(self):
        """
        Test to verify GET comment valid (Model and Serializer)
        """
        url = self.url + '?task={id}'.format(id=self.task.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        commentSerial = CommentSerializer(instance=self.comment)
        print(commentSerial.data)
        self.assertEqual(commentSerial.data, response_data['results'][0])

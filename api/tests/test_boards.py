import json

from users.models import CustomUser

from api.models import *
from api.serializers import *

from .authBase import AuthBaseTestCase



class BoardTestCase(AuthBaseTestCase):
    url = '/api/v1/boards'

    def setUp(self):
        super().setUp() # Authenticanting
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
          "due_date": "2019-11-11",
          "board": self.board,
        }
        self.task = Task.objects.create(**self.data_task)
        self.data_task['board'] = self.board.id


    def test_read_board_get(self):
        """
        Test to verify GET board valid (Model and Serializer)
        """
        url = self.url + '?project={id}'.format(id=self.project.id)
        response = self.client.get(url)
        print(response.status_code, response.content)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        print(response_data)
        boardSerial = BoardSerializer(instance=self.board)
        boardsSerial= [BoardSerializer(instance=x).data for x in self.boards]
        print(boardSerial.data)
        print(boardsSerial)
        self.assertEqual(boardsSerial, response_data['results'])

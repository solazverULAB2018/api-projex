from django.test import TestCase
from users.models import CustomUser

# Create your tests here.

class UserTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        CustomUser.objects.create_user(username="pablito", email="pablito@gmail.com")
        CustomUser.objects.create_user(username="tato", email="tato@gmail.com")

    def test_username(self):
        a = CustomUser.objects.get(username="pablito")
        self.assertEqual(a.username, "pablito")
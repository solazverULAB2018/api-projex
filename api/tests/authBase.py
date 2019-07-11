from rest_framework.test import APITestCase

from users.models import CustomUser


class AuthBaseTestCase(APITestCase):
    email = "@testuser.com"
    password = "12345Hola"

    def setUp(self):
        self.user = CustomUser.objects.create_user('user', 'user'+self.email, self.password)
        self.jefe = CustomUser.objects.create_user('jefe', 'jefe'+self.email, self.password)
        self.emp1 = CustomUser.objects.create_user('emp1', 'emp1'+self.email, self.password)
        self.emp2 = CustomUser.objects.create_user('emp2', 'emp2'+self.email, self.password)
        self.client.login(username='jefe', password=self.password)

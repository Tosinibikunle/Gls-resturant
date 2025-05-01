from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTests(TestCase):
    def test_create_user(self):
            user = User.objects.create_user(username='johndoe', password='secret123')
            self.assertEqual(user.username, 'johndoe')
            self.assertTrue(user.check_password('secret123'))
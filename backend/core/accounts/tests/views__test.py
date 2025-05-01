from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

class AccountsViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
                    'username': 'testuser',
                    'email': 'test@example.com',
                    'password': 'testpass123'
                     }

                                                                    def test_register_user(self):
                                                                            response = self.client.post('/api/accounts/register/', self.user_data)
                                                                                    self.assertEqual(response.status_code, 201)

                                                                                        def test_login_user(self):
                                                                                                User.objects.create_user(**self.user_data)
                                                                                                        response = self.client.post('/api/accounts/login/', {
                                                                                                                    'username': 'testuser',
                                                                                                                                'password': 'testpass123'
                                                                                                                                        })
                                                                                                                                                self.assertEqual(response.status_code, 200)
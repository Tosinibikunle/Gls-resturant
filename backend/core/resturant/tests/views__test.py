from rest_framework.test import APIClient
from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemViewTests(TestCase):
    def setUp(self):
       self.client = APIClient()

    def test_list_menu_items(self):
        MenuItem.objects.create(name='Burger', price=1200, available=True)
        response = self.client.get('/api/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

    def test_create_menu_item(self):
        data = {'name': 'Pizza', 'price': 2000, 'available': True}
        response = self.client.post('/api/restaurant/menu/', data)
        self.assertEqual(response.status_code, 201)
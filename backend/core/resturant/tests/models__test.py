from django.test import TestCase
from resturant.models import MenuItem

class MenuItemModelTests(TestCase):
    def test_create_menu_item(self):
            item = MenuItem.objects.create(name='Fried Rice', price=1500, available=True)
            self.assertEqual(item.name, 'Fried Rice')
            self.assertTrue(item.available)
from django.test import TestCase
from delivery.models import Delivery
from restaurant.models import Order  # Or your equivalent

class DeliveryModelTests(TestCase):
    def setUp(self):
      self.order = Order.objects.create(customer_name='Alice')

    def test_create_delivery(self):
      delivery = Delivery.objects.create(order=self.order, address='123 Road St', status='pending')
      self.assertEqual(delivery.status, 'pending')
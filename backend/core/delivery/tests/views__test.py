from django.test import TestCase
from rest_framework.test import APIClient
from delivery.models import Delivery
from restaurant.models import Order

class DeliveryViewTests(TestCase):
    def setUp(self):
            self.client = APIClient()
                    self.order = Order.objects.create(customer_name='Bob')

                        def test_create_delivery(self):
                                response = self.client.post('/api/delivery/', {
                                            'order': self.order.id,
                                                        'address': '456 Lane Way'
                                                                })
                                                                        self.assertEqual(response.status_code, 201)

                                                                            def test_update_delivery_status(self):
                                                                                    delivery = Delivery.objects.create(order=self.order, address='456 Lane Way', status='pending')
                                                                                            response = self.client.patch(f'/api/delivery/{delivery.id}/', {'status': 'delivered'})
                                                                                                    self.assertEqual(response.status_code, 200).
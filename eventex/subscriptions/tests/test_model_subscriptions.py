from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(name="Jose cordeiro",
                           cpf="12345678901",
                           email="cordjr@gmail.com",
                           phone="21-876876868668")
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an attribute created at """

        self.assertIsInstance(self.obj.created_at, datetime)
    def test_str(self):

        self.assertEqual("Jose cordeiro", str(self.obj))
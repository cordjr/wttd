from django.test import TestCase
from django.shortcuts import resolve_url as r

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r("home"))

    def test_get(self):
        """ GET / must return status code 200        """

        self.assertEqual(200, self.response.status_code)

    def test_must_use_template(self):
        """ Must use template index.h tml    """

        self.assertTemplateUsed(self.response, "index.html")

    def test_subscription_link(self):
        """Must have a subscriptoin link"""
        expected =  'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

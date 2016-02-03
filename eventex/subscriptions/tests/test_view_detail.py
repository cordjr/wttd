from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionTestGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='José Cordeiro',
                                               cpf='12345678901',
                                               email='cordjr@gmail.com',
                                               phone='9884182608')
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscripton = self.resp.context['subscription']
        self.assertIsInstance(subscripton, Subscription)

    def test_html(self):
        contents = (
            self.obj.name
            , self.obj.cpf
            , self.obj.email
            , self.obj.phone
        )
        with self.subTest():
            for expect in contents:
                self.assertContains(self.resp, expect)


class SubscriptonDetailNotFound(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:detail', 0))

    def test_not_found(self):
        self.assertEqual(404, self.resp.status_code)

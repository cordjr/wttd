import unittest

from django.test import TestCase
from django.core import mail
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get("/inscricao/")

    def test_get(self):
        """ Get /inscricao shoud return code 200         """

        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """ Should user subscriptions/subscription_form.html        """

        self.assertTemplateUsed(self.resp, "subscriptions/subscription_form.html")

    def test_html(self):
        """HTML must contain input tags """
        tags = (("<form", 1)
                , ("<input", 6)
                , ('type="text"', 3)
                , ('type="email"', 1)
                , ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Must contain csrf input"""

        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have form"""
        form = self.resp.context["form"]
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_fields(self):
        """Form must have 4 fields """
        form = self.resp.context["form"]
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Henrique Bastos", cpf="12345678901",
                    email="henrique@bastos.net", phone="98-12345-798901")

        self.resp = self.client.post("/inscricao/", data)

    def test_post(self):
        """Valid should redirect to '/inscricao'"""
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, '/inscricao/1/')

    def test_send_subscribe_email(self):
        """should send an subscribe email"""
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribedPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post("/inscricao/", {})

    def test_post(self):
        ''' verifica '''
        self.assertEqual(200, self.resp.status_code)


    def test_use_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_not_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())




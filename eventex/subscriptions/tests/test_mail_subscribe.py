from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribeMailValid(TestCase):
    def setUp(self):
        data = dict(name="Henrique Bastos", cpf="12345678901",
                    email="henrique@bastos.net", phone="98-12345-798901")

        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscricao'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_fromt(self):
        expect = settings.DEFAULT_FROM_EMAIL
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['henrique@bastos.net', settings.DEFAULT_FROM_EMAIL]
        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '98-12345-798901',
            'henrique@bastos.ne',
            'Henrique Bastos',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

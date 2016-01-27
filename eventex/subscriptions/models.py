from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('Cpf', max_length=11)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrção'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

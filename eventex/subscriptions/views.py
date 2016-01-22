from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(request, "subscriptions/subscription_form.html", {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    form.full_clean()
    message = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
    _send_mail('Confirmação de Inscricao',
               message,
               form.cleaned_data['email'], settings.DEFAULT_FROM_EMAIL)

    messages.success(request, 'Inscrção realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def _send_mail(subject, body, to, from_):
    mail.send_mail(subject, body, from_, [to, from_])

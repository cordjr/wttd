from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

from django.shortcuts import resolve_url as r


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, "subscriptions/subscription_form.html", {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    form.full_clean()
    subscription = Subscription.objects.create(**form.cleaned_data)
    message = render_to_string('subscriptions/subscription_email.txt', {'subscription': subscription})
    _send_mail('Confirmação de Inscricao',
               message,
               subscription.email, settings.DEFAULT_FROM_EMAIL)

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
        return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})
    except Subscription.DoesNotExist:
        raise Http404


def _send_mail(subject, body, to, from_):
    mail.send_mail(subject, body, from_, [to, from_])

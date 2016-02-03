from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


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
    subscription = Subscription.objects.create(**form.cleaned_data)
    message = render_to_string('subscriptions/subscription_email.txt', {'subscription': subscription})
    _send_mail('Confirmação de Inscricao',
               message,
               subscription.email, settings.DEFAULT_FROM_EMAIL)


    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
        return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})
    except Subscription.DoesNotExist:
        raise Http404



def _send_mail(subject, body, to, from_):
    mail.send_mail(subject, body, from_, [to, from_])

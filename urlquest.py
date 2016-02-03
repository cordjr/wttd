import os
from django.conf import settings
from django.core.urlresolvers import get_urlconf, set_urlconf, resolve, reverse
from django.conf.urls import url, include


def index(request): pass


def auth(request): pass


def list_(request): pass


def edit(request): pass


def new(request): pass


def delete(request): pass


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')

print('MEU ROOT URL CONF É ', settings.ROOT_URLCONF)
print('get_urlconf', get_urlconf())


class LendConf:
    def __init__(self, name):
        self.urlpatterns = [
            url(r'^(\d+)/$', edit, name='edit'),
            url(r'^new/$', new, name='new'),
            url(r'^delete/$', delete, name='delete'),
            url(r'^$', list_, name='list'),
        ]


class MySiteUrlConf:
    urlpatterns = [url(r'^$', index, name='index'),
                   url(r'^login/$', auth, kwargs={'action': 'login'}, name='login'),
                   url(r'^logout/$', auth, kwargs={'action': 'logout'}, name='logout'),
                   url(r'^groups/', include(LendConf('groups'), namespace='groups')),
                   url(r'^users/', include(LendConf('users'), namespace='users'))
                   ]


print('set_urlconf', MySiteUrlConf)

set_urlconf(MySiteUrlConf)

print('get_urlconf', get_urlconf())
print()
print()
print('Resolve:')
print(resolve('/'))
print(resolve('/login/'))
print(resolve('/logout/'))
print(resolve('/groups/'))
print(resolve('/groups/1/'))
print(resolve('/groups/new/'))
print(resolve('/groups/delete/'))
print(resolve('/users/'))
print(resolve('/users/1/'))
print(resolve('/users/new/'))
print(resolve('/users/delete/'))


print()
print('Reverse')
print(reverse('index'))
print(reverse('login'))
print(reverse('logout'))
print(reverse('groups:list'))
print(reverse('groups:edit', args=[1]))
print(reverse('groups:new'))
print(reverse('groups:delete'))
print(reverse('users:list'))
print(reverse('users:edit', args=[1]))
print(reverse('users:new'))
print(reverse('users:delete'))


from os.path import join, normpath
from .base import *

STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))

ALLOWED_HOSTS = [
'*'
    ]

STATIC_ROOT = normpath(join(SITE_ROOT, 'staticfiles'))
STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shopdb',
        'USER': 'aohshop',
        'PASSWORD':'aohshop15541365416',
        'HOST': 'localhost',
        'PORT': '',
    }
}

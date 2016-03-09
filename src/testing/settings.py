import os
import tempfile
import logging

from banter.conf.global_settings import *


RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

SECRET_KEY = 'testing'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'banter_test',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'banter_test',
    }
}

TEMPLATE_DIRS += (
    os.path.join(RESOURCES_DIR, 'templates'),
)

MEDIA_ROOT = tempfile.mkdtemp()
STATIC_ROOT = tempfile.mkdtemp()

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

COMPRESS_ENABLED = False
logging.disable(logging.CRITICAL)

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banter.settings')

from django.core.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
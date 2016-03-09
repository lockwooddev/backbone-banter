import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(PROJECT_DIR))

ROOT_URLCONF = 'banter.urls'
WSGI_APPLICATION = 'banter.wsgi.application'

SECRET_KEY = 'replacethis'
ALLOWED_HOSTS = []

DEBUG = TEMPLATE_DEBUG = False

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'banter@example.org'
EMAIL_SUBJECT_PREFIX = os.path.basename(PROJECT_DIR)

LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'banter.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    }
}

BOARD_LIST = [
    {'board': 'a', 'title': 'Anime & Manga'},
    {'board': 'b', 'title': 'Random'},
    {'board': 'c', 'title': 'Anime/Cute'},
    {'board': 'd', 'title': 'Hentai/Alternative'},
    {'board': 'e', 'title': 'Ecchi'},
    {'board': 'f', 'title': 'Flash'},
    {'board': 'g', 'title': 'Technology'},
    {'board': 'gif', 'title': 'Adult GIF'},
    {'board': 'h', 'title': 'Hentai'},
    {'board': 'hr', 'title': 'High Resolution'},
    {'board': 'k', 'title': 'Weapons'},
    {'board': 'm', 'title': 'Mecha'},
    {'board': 'o', 'title': 'Auto'},
    {'board': 'p', 'title': 'Photo'},
    {'board': 'r', 'title': 'Adult Requests'},
    {'board': 's', 'title': 'Sexy Beautiful Women'},
    {'board': 't', 'title': 'Torrents'},
    {'board': 'u', 'title': 'Yuri'},
    {'board': 'v', 'title': 'Video Games'},
    {'board': 'vg', 'title': 'Video Game Generals'},
    {'board': 'vr', 'title': 'Retro Games'},
    {'board': 'w', 'title': 'Anime/Wallpapers'},
    {'board': 'wg', 'title': 'Wallpapers/General'},
    {'board': 'i', 'title': 'Oekaki'},
    {'board': 'ic', 'title': 'Artwork/Critique'},
    {'board': 'r9k', 'title': 'ROBOT9001'},
    {'board': 's4s', 'title': 'Shit 4chan Says'},
    {'board': 'cm', 'title': 'Cute/Male'},
    {'board': 'hm', 'title': 'Handsome Men'},
    {'board': 'lgbt', 'title': 'LGBT'},
    {'board': 'y', 'title': 'Yaoi'},
    {'board': '3', 'title': '3DCG'},
    {'board': 'aco', 'title': 'Adult Cartoons'},
    {'board': 'adv', 'title': 'Advice'},
    {'board': 'an', 'title': 'Animals & Nature'},
    {'board': 'asp', 'title': 'Alternative Sports'},
    {'board': 'biz', 'title': 'Business & Finance'},
    {'board': 'cgl', 'title': 'Cosplay & EGL'},
    {'board': 'ck', 'title': 'Food & Cooking'},
    {'board': 'co', 'title': 'Comics & Cartoons'},
    {'board': 'diy', 'title': 'Do It Yourself'},
    {'board': 'fa', 'title': 'Fashion'},
    {'board': 'fit', 'title': 'Fitness'},
    {'board': 'gd', 'title': 'Graphic Design'},
    {'board': 'hc', 'title': 'Hardcore'},
    {'board': 'his', 'title': 'History & Humanities'},
    {'board': 'int', 'title': 'International'},
    {'board': 'jp', 'title': 'Otaku Culture'},
    {'board': 'lit', 'title': 'Literature'},
    {'board': 'mlp', 'title': 'Pony'},
    {'board': 'mu', 'title': 'Music'},
    {'board': 'n', 'title': 'Transportation'},
    {'board': 'news', 'title': 'Current News'},
    {'board': 'out', 'title': 'Outdoors'},
    {'board': 'po', 'title': 'Papercraft & Origami'},
    {'board': 'pol', 'title': 'Politically Incorrect'},
    {'board': 'sci', 'title': 'Science & Math'},
    {'board': 'soc', 'title': 'Cams & Meetups'},
    {'board': 'sp', 'title': 'Sports'},
    {'board': 'tg', 'title': 'Traditional Games'},
    {'board': 'toy', 'title': 'Toys'},
    {'board': 'trv', 'title': 'Travel'},
    {'board': 'tv', 'title': 'Television & Film'},
    {'board': 'vp', 'title': 'Pokémon'},
    {'board': 'wsg', 'title': 'Worksafe GIF'},
    {'board': 'wsr', 'title': 'Worksafe Requests'},
    {'board': 'x', 'title': 'Paranormal'},
]

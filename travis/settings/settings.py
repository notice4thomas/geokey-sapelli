"""GeoKey settings for Travis CI."""

import os.path
from geokey.core.settings.dev import *


DEFAULT_FROM_EMAIL = 'geokey@travis-ci.org'
ACCOUNT_EMAIL_VERIFICATION = 'optional'

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geokey',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'geokey_sapelli',
)

STATIC_URL = '/static/'

MEDIA_ROOT = normpath(join(dirname(dirname(abspath(__file__))), 'assets'))
MEDIA_URL = '/assets/'

WSGI_APPLICATION = 'settings.wsgi.application'

SAPELLI_JAR = 'sapelli-collector-cmdln-with-dependencies.jar'
SAPELLI_CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

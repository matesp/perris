""" Settings required by django-progressive-web-app. """
from django.conf import settings
import os

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates', 'serviceworker.js'))

# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'Mis perris')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'Adopcion de mascotas')
PWA_APP_ROOT_URL = getattr(settings, 'PWA_APP_ROOT_URL', '/')
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', 'rgb(162, 223, 192)')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_START_URL = getattr(settings, 'PWA_APP_START_URL', '/')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': '/static/img/icon_144.png',
        'sizes': '144x144'
    },
    {
        'src': '/static/img/icon_64.png',
        'sizes': '64x64'
    },
    {
        'src': '/static/img/icon_32.png',
        'sizes': '32x32'
    },
    {
        'src': '/static/img/favicon.png',
        'sizes': '16x16'
    }
])



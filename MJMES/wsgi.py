"""
WSGI config for MJMES project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.environ['MJMES.settings'] = (os.path.join(BASE_DIR,'mjmes/settings'))

# os.environ.setdefault("DJANDGO_SETTINGS_MODULE", "MJMES.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'MJMES.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

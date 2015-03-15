"""
WSGI config for MJMES project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'MJMES.settings'
sys.path.append(BASE_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

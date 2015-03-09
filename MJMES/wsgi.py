"""
WSGI config for MJMES project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os,sys
# os.environ.setdefault("DJANDGO_SETTINGS_MODULE", "MJMES.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'MJMES.settings'
sys.path.append(os.path.dirname(__file__))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

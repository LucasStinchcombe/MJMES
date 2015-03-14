"""
Django settings for MJMES project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4n-3y@4yg(4*rjsh5$&=x&jckgb(1m++j6ro^br*cxture40n6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'blog',
    'archives',
    'about',
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

ROOT_URLCONF = 'MJMES.urls'
WSGI_APPLICATION = 'MJMES.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# import dj_database_url
# DATABASES = {
#     'default' : dj_database_url.config()
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mjmes',
        'USER': 'root',
        'PASSWORD': 'mjmes',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)
FIXTURE_DIRS = (os.path.join(BASE_DIR, "templates/fixtures"),)


# MJMES Website Information
from django.contrib import admin
admin.site.site_header = 'MJMES Administration'
admin.site.title = 'MJMES'
MARKDOWN_EDITOR_SKIN = 'simple'

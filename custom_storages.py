from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class FixedS3BotoStorage(S3BotoStorage):
    def url(self, name):
        # Fix for django error abusing {% static %}
        url = super(FixedS3BotoStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url

StaticStorage = lambda: FixedS3BotoStorage( location=settings.STATICFILES_LOCATION )
MediaStorage = lambda: S3BotoStorage( location=settings.MEDIAFILES_LOCATION )

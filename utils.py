from django.conf import settings

from boto.s3.connection import S3Connection, OrdinaryCallingFormat
from storages.backends.s3boto import S3BotoStorage


class NibblerStorage(S3BotoStorage):
    """
    Storage backend for VMFarms http://nibbler.io

    The base `storages.backends.s3boto.S3BotoStorage` backend from django-storages
    could not be used as it did not allow a custom host or port to be specified.

    """

    def __init__(self, *args, **kwargs):
        super(NibblerStorage, self).__init__(*args, **kwargs)
        access_key, secret_key = self._get_access_keys()
        self.connection = S3Connection(
            access_key,
            secret_key,
            calling_format=OrdinaryCallingFormat(),
            host=getattr(settings, 'AWS_S3_CUSTOM_HOST', 'beta.nibbler.io'),
            port=getattr(settings, 'AWS_S3_CUSTOM_PORT', 8080)
        )

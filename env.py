import os
from importlib import import_module

VERSION = (0, 1)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Easily manage your python application settings for different environments'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/env.py'
__license__ = 'BSD'

try:
    from django.core.exceptions import ImproperlyConfigured
    ENVException = ImproperlyConfigured
except:
    ENVException = Exception

ENV = os.environ.get('SETTINGS_ENV')
if ENV is None:
    try:
        from local_env import ENV
    except:
        raise ENVException('Define ENV variable inside local_env.py or SETTINGS_ENV environment variable')

try:
    settings = import_module('%s_settings' % ENV)
    for k in dir(settings):
        if not k.startswith('__'):
            globals()[k] = getattr(settings, k)
except Exception, e:
    raise ENVException('Unable to import %s_settings.py with reason %s' % (ENV, str(e)))

VERSION = (0, 2, 1)
__version__ = '.'.join(map(str, VERSION[0:3])) + ''.join(VERSION[3:])
__description__ = 'Easily manage your python application settings for different environments'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/env.py'
__license__ = 'BSD'

import os
import sys
from importlib import import_module

try:
    from django.core.exceptions import ImproperlyConfigured
    ENVException = ImproperlyConfigured
except:
    ENVException = Exception

ENV = os.environ.get('SETTINGS_ENV')
if ENV is None:
    importer = sys._getframe(1).f_globals.get('__name__')
    try:
        if not importer:
            print 'Importer: None, set appropriate PYTHONPATH if you see error'
            from local_env import ENV
        else:
            parts = importer.split('.')
            parts = parts[:-1] if len(parts) > 1 else parts
            importer = '.'.join(parts)
            print 'Importer: %s' % importer
            ENV = getattr(import_module('%s.local_env' % importer), 'ENV')
    except Exception, e:
        raise ENVException('Define ENV variable inside local_env.py or SETTINGS_ENV environment variable')

try:
    print 'using ENV: %s, %s_settings must exist' % (ENV, ENV)
    settings = import_module('%s_settings' % ENV if not importer else '%s.%s_settings' % (importer, ENV))
    for k in dir(settings):
        if not k.startswith('__'):
            globals()[k] = getattr(settings, k)
except Exception, e:
    raise ENVException('Unable to import %s_settings.py with reason %s' % (ENV, str(e)))

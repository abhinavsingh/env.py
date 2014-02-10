from setuptools import setup

VERSION = (0, 1)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Easily manage your python application settings for different environments'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/env.py'
__license__ = 'BSD'

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: Microsoft',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
]

setup(
    name                = 'env.py',
    version             = __version__,
    description         = __description__,
    long_description    = open('README.md').read().strip(),
    author              = __author__,
    author_email        = __author_email__,
    url                 = __homepage__,
    license             = __license__,
    py_modules          = ['env',],
    install_requires    = [],
    classifiers         = classifiers
)

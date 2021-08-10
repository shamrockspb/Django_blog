from .base import *

import environ

env = environ.Env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default=[])
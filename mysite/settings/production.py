from .base import *

DATABASES = {
    
    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'blog',

        'USER': 'postgres',

        'PASSWORD': 'example',

        'HOST': 'postgres',

        'PORT': '5432',

    }
}

ALLOWED_HOSTS = ['shamrock-project.com']

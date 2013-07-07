import os
from os.path import dirname, abspath, join, exists

HERE = abspath( dirname(__file__) )

def setup_environ(settings=None):
    if exists( join(HERE, 'local.py') ):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    else:
        if exists( join(HERE, 'env') ):
            with open(join(HERE, 'env')) as file:
                settings = 'settings.%s' % open(file).read().strip()
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings or "settings.dev")

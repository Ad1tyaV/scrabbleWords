"""
WSGI config for scrabbleWords project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
from wordFinder import trieInit
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrabbleWords.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

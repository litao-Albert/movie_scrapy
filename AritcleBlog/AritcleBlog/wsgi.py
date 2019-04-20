"""
WSGI config for AritcleBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AritcleBlog.settings")

sys.path.append('C:\\Users\\黎涛\\PycharmProjects\\untitled')
sys.path.append('C:\\Users\\黎涛\AppData\\Local\\Programs\\Python\\Python35\\Lib')

application = get_wsgi_application()

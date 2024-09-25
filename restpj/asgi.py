"""
ASGI config for restpj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi_app.main import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restpj.settings')

django_asgi_app= get_asgi_application()
application=WSGIMiddleware(django_asgi_app)
application=fastapi_app


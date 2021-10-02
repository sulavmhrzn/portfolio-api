"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from decouple import config

if os.environ.get("ENV", config("ENV")) == "dev":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
elif os.environ.get("ENV", config("ENV")) == "prod":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")

application = get_wsgi_application()

from .base import *

DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS += ["debug_toolbar"]

# Django Debug Toolbar
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

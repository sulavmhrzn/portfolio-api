from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["*"]

DATABASES["default"] = dj_database_url.config(
    conn_max_age=600,
)

# Django Cloudinary Storage
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUD_NAME"),
    "API_KEY": config("API_KEY"),
    "API_SECRET": config("API_SECRET"),
}

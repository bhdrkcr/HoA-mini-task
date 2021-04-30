# Local Folder
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)

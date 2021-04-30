# Local Folder
from .base import *

# write emails to console, use this only in development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

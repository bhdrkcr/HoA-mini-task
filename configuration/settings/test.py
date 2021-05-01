# Local Folder
from .base import *

# dummy backend for emails use only in testing
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

# sqlite db for testing use only in testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test_db",
    }
}

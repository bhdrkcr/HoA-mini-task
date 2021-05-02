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

# testing recaptcha keys, use your own keys in production
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

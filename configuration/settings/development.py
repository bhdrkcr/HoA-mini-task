# Local Folder
from .base import *

# write emails to console, use this only in development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# testing recaptcha keys, use your own keys in production
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

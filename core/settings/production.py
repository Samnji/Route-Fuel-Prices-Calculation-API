from .base import *

DEBUG = False


# Production-specific settings
# Static files settings for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


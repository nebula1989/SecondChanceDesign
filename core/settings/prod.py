from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'secondchance.design',
    'www.secondchance.design',
    '54.90.219.106',
]

CSRF_TRUSTED_ORIGINS = [
    'https://secondchance.design',
    'https://www.secondchance.design',
]

# NGINX will serve from here
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# load production server
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost', 'localhost:85', '127.0.0.1', 'secondchance.design', 'www.secondchance.design', '54.90.219.106']
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'secondchance.design', 'www.secondchance.design', '54.90.219.106']
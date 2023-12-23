# load production server
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['http://secondchancedesign.com', 'secondchance.design', 'www.secondchance.design', 'http://www.secondchance.design', 'http://www.secondchance.design/admin', '54.90.219.106']
CSRF_TRUSTED_ORIGINS = ['http://secondchance.design', 'http://www.secondchance.design', 'http://www.secondchance.design/admin']

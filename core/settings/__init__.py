import os

# Default to 'dev' if DJANGO_ENV is not set
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .prod import *
else:
    from .dev import *


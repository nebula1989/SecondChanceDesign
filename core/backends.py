from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache
from django.conf import settings
from django.utils import timezone

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        ip_address = self.get_client_ip(request)

        # Get failed attempts for the IP address
        failed_attempts = cache.get(f'failed_login_attempts_{ip_address}', 0)

        if failed_attempts >= settings.MAX_LOGIN_ATTEMPTS - 1:
            # Lock the IP address for 3 minutes
            lock_time = timezone.now() + timezone.timedelta(minutes=3)
            cache.set(f'user_locked_{ip_address}', lock_time, timeout=180)

            # Reset failed login attempts counter
            cache.delete(f'failed_login_attempts_{ip_address}')
        else:
            # Increment failed login attempts
            cache.set(f'failed_login_attempts_{ip_address}', failed_attempts + 1)

        # Check if login is locked
        user_locked_until = cache.get(f'user_locked_{ip_address}')
        if user_locked_until and timezone.now() < user_locked_until:
            return None

        return super().authenticate(request, username=username, password=password, **kwargs)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

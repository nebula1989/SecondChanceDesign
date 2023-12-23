from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, re_path

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # Add the following re_path for the admin without trailing slash
    re_path(r'^admin$', lambda x: HttpResponseRedirect('/admin/')), 
    
    path('', include("apps.home.urls")),

]

# Ensure that this is configured to serve media files only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.home.views.error_404'
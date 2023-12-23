from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [         # Django admin route
    path('', include("apps.home.urls"))
    path('', include("apps.photo.urls"))

]

# Ensure that this is configured to serve media files only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.home.views.error_404'
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path, re_path, include
from django.contrib.sitemaps.views import sitemap
from apps.home.sitemaps import StaticViewSitemap
from django.contrib.sites.shortcuts import get_current_site

sitemaps = {
    'static': StaticViewSitemap(),
}

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /venv/",
        "Allow: /apps/",
        "Allow: /core/"
    ]
    
    # Dynamically add sitemap URL
    current_site = get_current_site(request)
    sitemap_url = f"Sitemap: https://secondchance.design/sitemap.xml"
    lines.append(sitemap_url)
    
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # Add the following re_path for the admin without trailing slash
    re_path(r'^admin$', lambda x: HttpResponseRedirect('/admin/')), 
    
    path('', include("apps.home.urls")),
    path('robots.txt', robots_txt),  # URL for robots.txt
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

# Ensure that this is configured to serve media files only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.home.views.error_404'
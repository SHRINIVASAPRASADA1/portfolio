from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('access/pass=root', admin.site.urls),
    re_path(r'^robots\.txt', include('robots.urls')),
    path('', include("app1.urls")),
    # path(r'^one/$', RedirectView.as_view(url='/another/')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

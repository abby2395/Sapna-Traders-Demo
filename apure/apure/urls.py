from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
import store.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('store.urls', namespace = 'store')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
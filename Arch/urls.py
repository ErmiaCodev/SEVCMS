from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls')),
    path('', include('app.urls')),
    path('message/', include('messager.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

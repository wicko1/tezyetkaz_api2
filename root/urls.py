from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
                  path('api/v1/', include('apps.urls')),
                  path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path("admin/", admin.site.urls),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

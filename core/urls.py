from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns_api_v1 = [
        path('', include('reserve.urls_api'), name='reservations'),
]

urlpatterns = [
    # URLs admin
    path('admin/', admin.site.urls, name="admin_urls"),

    # URLs drf_spectacular
    path('api/v1/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/v1/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # URLs api
    path('api/v1/', include(urlpatterns_api_v1), name="api_urls"),

]

# _______________________________ Static Config __________________________________________

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

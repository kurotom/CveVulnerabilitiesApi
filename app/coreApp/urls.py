from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='Api CVE Vulnerabilities',
        default_version='v0.1',
        description='Api REST CVE',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=''),
        license=openapi.License(name="GPL-3.0 license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('backend/', admin.site.urls),
    path("api/", include("api.urls")),
    path('doc/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-redoc'
    ),
]


handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'

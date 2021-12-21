from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions

from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Survey API",
      default_version='v1',
      description="Документация для приложения для проведения опросов",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]

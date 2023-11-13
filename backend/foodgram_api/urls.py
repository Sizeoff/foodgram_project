from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')),

    path('api/', include('users.urls')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="Foodgram - Продуктовый помощник",
        default_version='v1',
        description='''Документация для приложения
                    "Foodgram - Продуктовый помощник"''',
        contact=openapi.Contact(email="vladsizov96@yandex.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

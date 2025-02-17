"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from categorias.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description='Documentacion de la API del Blog',
        terms_of_service='',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD Licence')
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    #swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #app users
    path('api/',include('users.api.router')),

    #app categorias
    path('api/',include(router_categories.urls)),

    #app posts
    path('api/',include(router_posts.urls)),

    #app comments
    path('api/',include(router_comments.urls)),
]

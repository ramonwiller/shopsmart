from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import PriceViewSet, ProductViewSet, StoreViewSet

router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'prices', PriceViewSet, basename='prices')


schema_view = get_schema_view(
    openapi.Info(
        title="Shop Smart",
        default_version='v1',
        description="A Shop Smart é uma plataforma colaborativa que fornece acesso a informações atualizadas sobre produtos e preços, alimentada pelo esforço da comunidade. Nesta API, os desenvolvedores têm acesso a uma ampla variedade de dados, incluindo detalhes de produtos e preços oferecidos em diversos supermercados.",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/tokens/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]

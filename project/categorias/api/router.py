from rest_framework.routers import DefaultRouter
from .views import *

router_categories = DefaultRouter()

router_categories.register(prefix='categories',basename='categories',viewset=CategoryApiViewSet)
from comments.api.views import CommentApiViewSet
from rest_framework.routers import DefaultRouter

router_comments = DefaultRouter()

router_comments.register(prefix='comments',basename='comments',viewset=CommentApiViewSet)
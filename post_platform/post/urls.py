from rest_framework.routers import DefaultRouter
from .views import PostAPIView, CommentAPIView

router = DefaultRouter()
router.register(r'posts', PostAPIView, basename='post')
router.register(r'comments', CommentAPIView, basename='comment')
urlpatterns = router.urls

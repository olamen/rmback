from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, PlaylistViewSet, ShowViewSet, SongViewSet, TagViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'tags', TagViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'shows', ShowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

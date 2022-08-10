from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, ArticleViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('article', ArticleViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
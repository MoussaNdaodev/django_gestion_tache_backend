from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjetViewSet

router = DefaultRouter()
router.register(r'', ProjetViewSet, basename='projet')

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipeViewSet

router = DefaultRouter()
router.register(r'', EquipeViewSet, basename='equipe')

urlpatterns = [
    path('', include(router.urls)),
]
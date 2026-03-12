from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MesTachesView, TacheViewSet

router = DefaultRouter()
router.register(r'', TacheViewSet, basename='tache')

urlpatterns = [
    path('mes-taches/', MesTachesView.as_view()),
    path('', include(router.urls)),
]
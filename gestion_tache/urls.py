from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from gestion_tache import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/utilisateurs/', include('utilisateur.urls')),
    path('api/projets/', include('projet.urls')),
    path('api/equipes/', include('equipe.urls')),
    path('api/taches/', include('tache.urls')),

    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
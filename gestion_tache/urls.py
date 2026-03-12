from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from utilisateur.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/utilisateurs/',  include('utilisateur.urls')),
    path('api/projets/',       include('projet.urls')),
    path('api/equipes/',       include('equipe.urls')),
    path('api/taches/',        include('tache.urls')),
    path('api/notifications/', include('notification.urls')),
    path('api/statistiques/',  include('evaluation.urls')),
    path('api/login/',         CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
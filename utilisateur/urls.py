from django.urls import path
from .views import (
    RegisterView, ProfilView, UpdateProfilView,
    ChangePasswordView, UtilisateurListView,
    UtilisateurDetailView, UtilisateurDeleteView
)

urlpatterns = [
    path('register/',        RegisterView.as_view()),
    path('profil/',          ProfilView.as_view()),
    path('profil/update/',   UpdateProfilView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('',                 UtilisateurListView.as_view()),
    path('<int:pk>/',        UtilisateurDetailView.as_view()),
    path('<int:pk>/delete/', UtilisateurDeleteView.as_view()),
]
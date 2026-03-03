from django.urls import path
from .views import RegisterView, ProfilView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profil/', ProfilView.as_view()),
]
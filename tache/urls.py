from django.urls import path
from .views import MesTachesView, TacheCreateView

urlpatterns = [
    path('mes-taches/', MesTachesView.as_view()),
    path('create/', TacheCreateView.as_view()),
]
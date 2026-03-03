from django.urls import path
from .views import StatistiqueListCreateView, StatistiqueDetailView, PrimeListCreateView, PrimeDetailView

urlpatterns = [
    path('stats/', StatistiqueListCreateView.as_view()),
    path('stats/<int:pk>/', StatistiqueDetailView.as_view()),
    path('primes/', PrimeListCreateView.as_view()),
    path('primes/<int:pk>/', PrimeDetailView.as_view()),
]

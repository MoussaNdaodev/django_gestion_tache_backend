from django.urls import path
from .views import StatistiqueListView, PrimeListView, RecalculerStatsView, DashboardStatsView

urlpatterns = [
    path('', StatistiqueListView.as_view()),
    path('primes/', PrimeListView.as_view()),
    path('recalculer/', RecalculerStatsView.as_view()),
    path('dashboard/', DashboardStatsView.as_view()),
]
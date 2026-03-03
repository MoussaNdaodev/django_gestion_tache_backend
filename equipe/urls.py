from django.urls import path
from .views import EquipeListCreateView, EquipeDetailView

urlpatterns = [
    path('', EquipeListCreateView.as_view()),
    path('<int:pk>/', EquipeDetailView.as_view()),
]
from django.urls import path
from .views import ProjetListCreateView, ProjetDetailView

urlpatterns = [
    path('', ProjetListCreateView.as_view()),
    path('<int:pk>/', ProjetDetailView.as_view()),
]
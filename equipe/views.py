from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Equipe
from .serializers import EquipeSerializer

class EquipeListCreateView(generics.ListCreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated]


class EquipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated]
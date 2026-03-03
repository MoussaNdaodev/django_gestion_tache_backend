from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Projet
from .serializers import ProjetSerializer
from .permissions import IsProjectCreator

class ProjetListCreateView(generics.ListCreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Projet.objects.filter(createur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(createur=self.request.user)


class ProjetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [IsAuthenticated, IsProjectCreator]

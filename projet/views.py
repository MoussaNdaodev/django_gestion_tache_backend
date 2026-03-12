from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Projet
from .serializers import ProjetSerializer
from .permissions import IsProjectCreator
from tache.models import Tache
from tache.serializers import TacheSerializer
from equipe.models import Equipe
from equipe.serializers import EquipeSerializer


class ProjetViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetSerializer
    permission_classes = [IsAuthenticated, IsProjectCreator]

    def get_queryset(self):
        return Projet.objects.filter(
            createur=self.request.user
        ).prefetch_related('taches', 'equipes')

    def perform_create(self, serializer):
        serializer.save(createur=self.request.user)

    @action(detail=True, methods=['get'], url_path='taches')
    def taches(self, request, pk=None):
        projet = self.get_object()
        taches = Tache.objects.filter(projet=projet).select_related('assigne_a')
        serializer = TacheSerializer(taches, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='equipes')
    def equipes(self, request, pk=None):
        projet = self.get_object()
        equipes = Equipe.objects.filter(projet=projet).prefetch_related('membres')
        serializer = EquipeSerializer(equipes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='stats')
    def stats(self, request, pk=None):
        projet = self.get_object()
        return Response({
            'total':    projet.taches.count(),
            'a_faire':  projet.taches.filter(statut='a_faire').count(),
            'en_cours': projet.taches.filter(statut='en_cours').count(),
            'termine':  projet.taches.filter(statut='termine').count(),
        })
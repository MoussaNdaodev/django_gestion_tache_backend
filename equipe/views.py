from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Equipe
from .serializers import EquipeSerializer
from utilisateur.models import Utilisateur
from utilisateur.serializers import RegisterSerializer


class EquipeViewSet(viewsets.ModelViewSet):
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Equipe.objects.filter(
            membres=self.request.user
        ).select_related('projet').prefetch_related('membres')

    @action(detail=True, methods=['post'], url_path='ajouter-membre')
    def ajouter_membre(self, request, pk=None):
        equipe = self.get_object()
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id requis'}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(Utilisateur, pk=user_id)
        if equipe.membres.filter(pk=user_id).exists():
            return Response({'error': 'Cet utilisateur est déjà membre'}, status=status.HTTP_400_BAD_REQUEST)
        equipe.membres.add(user)
        return Response({'message': 'Membre ajouté avec succès'})

    @action(detail=True, methods=['delete'], url_path='supprimer-membre/(?P<user_id>[^/.]+)')
    def supprimer_membre(self, request, pk=None, user_id=None):
        equipe = self.get_object()
        if not equipe.membres.filter(pk=user_id).exists():
            return Response({'error': 'Utilisateur non membre'}, status=status.HTTP_404_NOT_FOUND)
        equipe.membres.remove(user_id)
        return Response({'message': 'Membre supprimé avec succès'})

    @action(detail=True, methods=['get'], url_path='membres')
    def membres(self, request, pk=None):
        equipe = self.get_object()
        serializer = RegisterSerializer(equipe.membres.all(), many=True)
        return Response(serializer.data)
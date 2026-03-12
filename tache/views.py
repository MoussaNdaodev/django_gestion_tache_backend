from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Tache
from .serializers import TacheSerializer


class MesTachesView(generics.ListAPIView):
    serializer_class = TacheSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Tache.objects.filter(
            assigne_a=self.request.user
        ).select_related('projet', 'assigne_a')
        statut = self.request.query_params.get('statut')
        priorite = self.request.query_params.get('priorite')
        if statut:
            qs = qs.filter(statut=statut)
        if priorite:
            qs = qs.filter(priorite=priorite)
        return qs


class TacheViewSet(viewsets.ModelViewSet):
    serializer_class = TacheSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tache.objects.select_related('projet', 'assigne_a').all()

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True, methods=['patch'], url_path='changer-statut')
    def changer_statut(self, request, pk=None):
        tache = self.get_object()
        statut = request.data.get('statut')
        if statut not in ['a_faire', 'en_cours', 'termine']:
            return Response(
                {'error': 'Statut invalide. Valeurs acceptées : a_faire, en_cours, termine'},
                status=status.HTTP_400_BAD_REQUEST
            )
        tache.statut = statut
        tache.save()
        return Response({'message': f'Statut changé en {statut}'})
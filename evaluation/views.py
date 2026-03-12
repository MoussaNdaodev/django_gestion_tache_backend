from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Statistique, Prime
from .serializers import StatistiqueSerializer, PrimeSerializer
from .utils import calculer_statistiques


class StatistiqueListView(generics.ListAPIView):
    serializer_class = StatistiqueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Statistique.objects.filter(utilisateur=self.request.user)
        annee = self.request.query_params.get('annee')
        trimestre = self.request.query_params.get('trimestre')
        if annee:
            qs = qs.filter(annee=annee)
        if trimestre:
            qs = qs.filter(trimestre=trimestre)
        return qs


class PrimeListView(generics.ListAPIView):
    serializer_class = PrimeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prime.objects.filter(utilisateur=self.request.user)


class RecalculerStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        stat = calculer_statistiques(request.user)
        return Response(StatistiqueSerializer(stat).data, status=status.HTTP_200_OK)


class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        now = timezone.now()
        annee = int(request.query_params.get('annee', now.year))
        trimestre = (now.month - 1) // 3 + 1

        stat_courante = Statistique.objects.filter(
            utilisateur=user, annee=annee, trimestre=trimestre
        ).first()

        historique = Statistique.objects.filter(
            utilisateur=user, annee=annee
        ).order_by('trimestre')

        primes = Prime.objects.filter(utilisateur=user, annee=annee)

        return Response({
            'nb_taches_total': stat_courante.nb_taches_total if stat_courante else 0,
            'nb_taches_terminees_delai': stat_courante.nb_taches_terminees_delai if stat_courante else 0,
            'taux_realisation': stat_courante.taux_realisation if stat_courante else 0.0,
            'annee': annee,
            'trimestre': trimestre,
            'primes': PrimeSerializer(primes, many=True).data,
            'historique_trimestriel': StatistiqueSerializer(historique, many=True).data,
        })
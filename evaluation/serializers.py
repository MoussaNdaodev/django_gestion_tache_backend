from rest_framework import serializers
from .models import Statistique, Prime


class StatistiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistique
        fields = '__all__'
        read_only_fields = ['utilisateur', 'date_calcul']


class PrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prime
        fields = '__all__'
        read_only_fields = ['utilisateur', 'date_attribution']


class StatsDashboardSerializer(serializers.Serializer):
    nb_taches_total = serializers.IntegerField()
    nb_taches_terminees_delai = serializers.IntegerField()
    taux_realisation = serializers.FloatField()
    annee = serializers.IntegerField()
    trimestre = serializers.IntegerField()
    primes = PrimeSerializer(many=True)
    historique_trimestriel = StatistiqueSerializer(many=True)
from rest_framework import serializers
from .models import Statistique, Prime

class StatistiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistique
        fields = '__all__'

class PrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prime
        fields = '__all__'

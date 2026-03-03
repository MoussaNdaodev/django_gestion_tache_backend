from rest_framework import serializers
from .models import Projet

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = ['id', 'titre', 'description', 'date_creation', 'date_fin',
                  'fichiers', 'images', 'createur']
        read_only_fields = ['createur', 'date_creation']
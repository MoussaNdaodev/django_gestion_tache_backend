from rest_framework import serializers
from .models import Projet


class ProjetSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField()

    class Meta:
        model = Projet
        fields = ['id', 'titre', 'description', 'date_creation',
                  'date_fin', 'fichiers', 'images', 'createur', 'stats']
        read_only_fields = ['createur', 'date_creation']

    def get_stats(self, obj):
        return {
            'total':    obj.taches.count(),
            'a_faire':  obj.taches.filter(statut='a_faire').count(),
            'en_cours': obj.taches.filter(statut='en_cours').count(),
            'termine':  obj.taches.filter(statut='termine').count(),
        }
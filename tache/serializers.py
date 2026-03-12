from rest_framework import serializers
from .models import Tache
from utilisateur.serializers import ProfilSerializer


class TacheSerializer(serializers.ModelSerializer):
    assigne_a_detail = ProfilSerializer(source='assigne_a', read_only=True)

    class Meta:
        model = Tache
        fields = [
            'id', 'titre', 'description', 'date_limite',
            'statut', 'priorite', 'date_creation',
            'projet', 'assigne_a', 'assigne_a_detail'
        ]

    def validate(self, data):
        request = self.context.get('request')
        projet = data.get('projet')
        assignee = data.get('assigne_a')

        if not projet or not assignee:
            return data

        if projet.createur != request.user:
            raise serializers.ValidationError("Seul le créateur peut créer une tâche.")

        if not projet.equipes.filter(membres=assignee).exists():
            raise serializers.ValidationError("Utilisateur non membre de l'équipe.")

        if request.user.role == 'etudiant' and assignee.role == 'professeur':
            raise serializers.ValidationError("Un étudiant ne peut pas assigner un professeur.")

        return data
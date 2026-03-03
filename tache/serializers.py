from rest_framework import serializers
from .models import Tache

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'

    def validate(self, data):
        request = self.context['request']
        projet = data['projet']
        assignee = data['assigne_a']

        if projet.createur != request.user:
            raise serializers.ValidationError("Seul le créateur peut créer une tâche")

        if not projet.equipes.filter(membres=assignee).exists():
            raise serializers.ValidationError("Utilisateur non membre de l'équipe")

        if request.user.role == 'etudiant' and assignee.role == 'professeur':
            raise serializers.ValidationError("Un étudiant ne peut pas assigner un professeur")

        return data
from rest_framework import serializers
from .models import Equipe


class EquipeSerializer(serializers.ModelSerializer):
    nombre_membres = serializers.SerializerMethodField()

    class Meta:
        model = Equipe
        fields = ['id', 'nom_equipe', 'projet', 'membres', 'nombre_membres']

    def get_nombre_membres(self, obj):
        return obj.membres.count()
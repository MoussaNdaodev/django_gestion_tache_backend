from rest_framework import serializers
from .models import Utilisateur

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur
        fields = ['id','nom','prenom','email','avatar','role','password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Utilisateur(**validated_data)
        user.set_password(password)
        user.save()
        return user



class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id','nom','prenom','email','avatar','role']
        read_only_fields = ['role']
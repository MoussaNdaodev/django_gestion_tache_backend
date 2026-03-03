from django.db import models
from projet.models import Projet
from utilisateur.models import Utilisateur

class Equipe(models.Model):
    nom_equipe = models.CharField(max_length=200)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='equipes')
    membres = models.ManyToManyField(Utilisateur, related_name='equipes')

    def __str__(self):
        return self.nom_equipe
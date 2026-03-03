from django.db import models
from projet.models import Projet
from utilisateur.models import Utilisateur

class Tache(models.Model):
    STATUTS = (
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    )

    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_limite = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUTS, default='a_faire')
    date_creation = models.DateTimeField(auto_now_add=True)

    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    assigne_a = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='taches')

    
    def est_proche_echeance(self):
        today = date.today()
        return (self.date_limite - today).days <= 1 and self.statut != 'termine'
    def __str__(self):
        return self.titre
from django.db import models
from projet.models import Projet
from utilisateur.models import Utilisateur


class Tache(models.Model):
    STATUTS = (
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    )
    PRIORITES = (
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    )

    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_limite = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUTS, default='a_faire')
    priorite = models.CharField(max_length=20, choices=PRIORITES, default='moyenne')
    date_creation = models.DateTimeField(auto_now_add=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    assigne_a = models.ForeignKey(
        Utilisateur, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='taches'
    )

    class Meta:
        ordering = ['date_limite']

    def __str__(self):
        return self.titre
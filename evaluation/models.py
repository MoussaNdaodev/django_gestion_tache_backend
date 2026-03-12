from django.db import models
from utilisateur.models import Utilisateur


class Statistique(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='statistiques')
    annee = models.IntegerField()
    trimestre = models.IntegerField()
    nb_taches_total = models.IntegerField(default=0)
    nb_taches_terminees_delai = models.IntegerField(default=0)
    taux_realisation = models.FloatField(default=0)
    date_calcul = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('utilisateur', 'annee', 'trimestre')
        ordering = ['annee', 'trimestre']

    def __str__(self):
        return f"{self.utilisateur} - {self.annee} T{self.trimestre} - {self.taux_realisation}%"


class Prime(models.Model):
    TYPES = (
        ('90%', 'Prime 90%'),
        ('100%', 'Prime 100%'),
    )
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='primes')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_prime = models.CharField(max_length=10, choices=TYPES)
    annee = models.IntegerField(default=0)
    trimestre = models.IntegerField(default=0)
    date_attribution = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'type_prime', 'annee', 'trimestre')
        ordering = ['-date_attribution']

    def __str__(self):
        return f"{self.utilisateur} - {self.type_prime} - {self.annee} T{self.trimestre}"
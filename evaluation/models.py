from django.db import models
from utilisateur.models import Utilisateur


class Statistique(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='statistiques')
    annee = models.IntegerField()
    trimestre = models.IntegerField()
    nb_taches_total = models.IntegerField(default=0)
    nb_taches_terminees_delai = models.IntegerField(default=0)
    taux_realisation = models.FloatField(default=0)


class Prime(models.Model):
    TYPES = (
        ('90%', 'Prime 90%'),
        ('100%', 'Prime 100%'),
    )

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='primes')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    type_prime = models.CharField(max_length=10, choices=TYPES)
    date_attribution = models.DateTimeField(auto_now_add=True)
from django.db import models
from utilisateur.models import Utilisateur


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateField(blank=True, null=True)
    fichiers = models.FileField(upload_to='projet/fichiers/', blank=True, null=True)
    images = models.ImageField(upload_to='projet/images/', blank=True, null=True)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projets')

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre
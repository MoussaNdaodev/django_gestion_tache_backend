from django.db import models
from tache.models import Tache
from utilisateur.models import Utilisateur


class Notification(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='notifications')
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    est_lu = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"Notif — {self.utilisateur.email} — {self.tache.titre}"
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from .models import Tache
from evaluation.utils import calculer_statistiques


@receiver(post_save, sender=Tache)
def maj_statistiques_sur_tache(sender, instance, **kwargs):
    if instance.assigne_a:
        calculer_statistiques(instance.assigne_a)


@receiver(post_save, sender=Tache)
def verifier_echeance_sur_save(sender, instance, **kwargs):
    if not instance.assigne_a or not instance.date_limite:
        return
    if instance.statut in ['a_faire', 'en_cours']:
        now = timezone.now().date()
        jours_avant = getattr(settings, 'NOTIFICATION_DAYS_BEFORE', 2)
        date_limite = instance.date_limite
        if hasattr(date_limite, 'date') and callable(date_limite.date):
            date_limite = date_limite.date()
        if date_limite <= now + timezone.timedelta(days=jours_avant):
            from notification.utils import envoyer_notification
            envoyer_notification(instance)
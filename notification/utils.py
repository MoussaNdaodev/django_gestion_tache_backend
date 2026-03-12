from datetime import date
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from tache.models import Tache
from .models import Notification


def _get_date(valeur):
    """Normalise date ou datetime en date."""
    return valeur.date() if hasattr(valeur, 'date') and callable(valeur.date) else valeur


def envoyer_notification(tache):
    # Évite les doublons sur la même journée
    if Notification.objects.filter(
        tache=tache,
        utilisateur=tache.assigne_a,
        date_creation__date=timezone.now().date()
    ).exists():
        return

    date_limite = _get_date(tache.date_limite)
    jours_restants = (date_limite - timezone.now().date()).days

    message = (
        f"Bonjour {tache.assigne_a.prenom} {tache.assigne_a.nom},\n\n"
        f"La tâche « {tache.titre} » arrive à échéance dans {jours_restants} jour(s) "
        f"(le {date_limite.strftime('%d/%m/%Y')}).\n\n"
        f"Statut actuel : {tache.get_statut_display()}\n"
        f"Projet : {tache.projet.titre}\n\n"
        f"Connectez-vous pour la compléter à temps.\n\n"
        f"— Équipe ESMT"
    )

    Notification.objects.create(
        utilisateur=tache.assigne_a,
        tache=tache,
        message=message
    )

    try:
        send_mail(
            subject=f"⏰ Échéance dans {jours_restants}j : {tache.titre}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[tache.assigne_a.email],
            fail_silently=False
        )
        print(f"[EMAIL] Envoyé à {tache.assigne_a.email}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")


def verifier_taches_proches():
    now = timezone.now().date()
    jours_avant = getattr(settings, 'NOTIFICATION_DAYS_BEFORE', 2)
    date_seuil = now + timezone.timedelta(days=jours_avant)

    taches = Tache.objects.filter(
        statut__in=['a_faire', 'en_cours'],
        date_limite__lte=date_seuil,
        date_limite__gte=now,
        assigne_a__isnull=False
    ).select_related('assigne_a', 'projet')

    for tache in taches:
        envoyer_notification(tache)

    return taches.count()
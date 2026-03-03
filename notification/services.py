from django.core.mail import send_mail

from tache.models import Tache
from .models import Notification

def envoyer_notification(tache):

    message = f"La tâche '{tache.titre}' arrive bientôt à échéance."

    # Créer notification en base
    Notification.objects.create(
        utilisateur=tache.assigne_a,
        tache=tache,
        message=message
    )

    # Envoyer email
    send_mail(
        subject="Tâche proche échéance",
        message=message,
        from_email="admin@gestion.com",
        recipient_list=[tache.assigne_a.email],
        fail_silently=True
    )
    

def verifier_taches_proches():

    taches = Tache.objects.filter(statut__in=['a_faire','en_cours'])

    for t in taches:
        if t.est_proche_echeance():
            envoyer_notification(t)
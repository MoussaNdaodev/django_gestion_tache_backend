from datetime import datetime
from tache.models import Tache
from .models import Prime, Statistique

def calculer_statistiques(utilisateur):

    now = datetime.now()
    annee = now.year
    trimestre = (now.month - 1) // 3 + 1

    taches = Tache.objects.filter(assigne_a=utilisateur)

    total = taches.count()

    terminees_delai = taches.filter(
        statut='termine',
        date_limite__gte=datetime.now().date()
    ).count()

    taux = (terminees_delai / total * 100) if total > 0 else 0
    if taux >= 100:
        Prime.objects.get_or_create(
            utilisateur=utilisateur,
            type_prime='100%',
            defaults={'montant': 100000}
        )

    elif taux >= 90:
        Prime.objects.get_or_create(
            utilisateur=utilisateur,
            type_prime='90%',
            defaults={'montant': 30000}
        )

    stat, created = Statistique.objects.update_or_create(
        utilisateur=utilisateur,
        annee=annee,
        trimestre=trimestre,
        defaults={
            'nb_taches_total': total,
            'nb_taches_terminees_delai': terminees_delai,
            'taux_realisation': taux
        }
    )

    return stat
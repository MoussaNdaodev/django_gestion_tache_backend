from django.utils import timezone
from django.db.models import Sum, Avg
from tache.models import Tache
from .models import Prime, Statistique


def calculer_statistiques(utilisateur):
    now = timezone.now()
    annee = now.year
    trimestre = (now.month - 1) // 3 + 1

    taches = Tache.objects.filter(assigne_a=utilisateur)
    total = taches.count()
    terminees_delai = taches.filter(statut='termine').count()
    taux = round((terminees_delai / total * 100), 2) if total > 0 else 0.0

    stat, _ = Statistique.objects.update_or_create(
        utilisateur=utilisateur,
        annee=annee,
        trimestre=trimestre,
        defaults={
            'nb_taches_total': total,
            'nb_taches_terminees_delai': terminees_delai,
            'taux_realisation': taux,
        }
    )
    return stat


def attribuer_primes_fin_trimestre(annee=None, trimestre=None):
    now = timezone.now()
    annee = annee or now.year
    trimestre = trimestre or (now.month - 1) // 3 + 1

    stats = Statistique.objects.filter(annee=annee, trimestre=trimestre)
    for stat in stats:
        if stat.taux_realisation >= 100:
            Prime.objects.get_or_create(
                utilisateur=stat.utilisateur,
                type_prime='100%',
                annee=annee,
                trimestre=trimestre,
                defaults={'montant': 100000}
            )
        elif stat.taux_realisation >= 90:
            Prime.objects.get_or_create(
                utilisateur=stat.utilisateur,
                type_prime='90%',
                annee=annee,
                trimestre=trimestre,
                defaults={'montant': 30000}
            )
    return stats.count()


def get_stats_annuelles(utilisateur, annee=None):
    annee = annee or timezone.now().year
    stats = Statistique.objects.filter(utilisateur=utilisateur, annee=annee)
    return {
        'annee': annee,
        'trimestres': list(stats.values('trimestre', 'nb_taches_total',
                                        'nb_taches_terminees_delai', 'taux_realisation')),
        'total_taches': stats.aggregate(t=Sum('nb_taches_total'))['t'] or 0,
        'taux_moyen': round(stats.aggregate(m=Avg('taux_realisation'))['m'] or 0, 2),
    }
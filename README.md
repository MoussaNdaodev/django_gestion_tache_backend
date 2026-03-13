# Gestion des Tâches Collaboratives — ESMT

Application web de gestion de tâches collaboratives développée dans le cadre du projet de fin de module. Elle permet aux enseignants et étudiants de gérer des projets, des tâches, des équipes, et de suivre les performances via un système de statistiques et de primes.

**Stack :** Django REST Framework (Python) + Angular (TypeScript)  
**Base de données :** SQLite  
**Authentification :** JWT (djangorestframework-simplejwt)

---

## Table des matières

1. [Prérequis](#prérequis)
2. [Installation](#installation)
3. [Modèles de données](#modèles-de-données)
4. [Routes API](#routes-api)

---

## Prérequis

- Python 3.12
- Node.js 18+
- pip

---

## Installation

### Backend (Django)

```bash
# Cloner le projet
git clone https://github.com/MoussaNdaodev/django_gestion_tache_backend.git

# Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un compte administrateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

L'API est accessible sur `http://localhost:8000`.  
La base de données `db.sqlite3` est créée automatiquement à la racine du projet.

### Frontend (Angular)

```bash
# Cloner le projet
git clone https://github.com/MoussaNdaodev/django_gestion_tache_frontend.git

# Installer les dépendances
npm install

# Lancer le serveur
ng serve
```

L'application est accessible sur `http://localhost:4200`.

---

## Modèles de données

### Utilisateur
| Champ | Type | Description |
|---|---|---|
| `email` | EmailField | Identifiant unique (remplace le username) |
| `nom` | CharField | Nom de famille |
| `prenom` | CharField | Prénom |
| `role` | CharField | `etudiant` ou `professeur` |
| `avatar` | ImageField | Photo de profil |

### Projet
| Champ | Type | Description |
|---|---|---|
| `titre` | CharField | Titre du projet |
| `description` | TextField | Description détaillée |
| `date_fin` | DateField | Date limite |
| `createur` | FK → Utilisateur | Propriétaire du projet |
| `fichiers` | FileField | Fichier joint |
| `images` | ImageField | Image du projet |

### Equipe
| Champ | Type | Description |
|---|---|---|
| `nom_equipe` | CharField | Nom de l'équipe |
| `projet` | FK → Projet | Projet associé |
| `membres` | M2M → Utilisateur | Membres de l'équipe |

### Tache
| Champ | Type | Description |
|---|---|---|
| `titre` | CharField | Titre de la tâche |
| `description` | TextField | Description |
| `date_limite` | DateField | Échéance |
| `statut` | CharField | `a_faire`, `en_cours`, `termine` |
| `priorite` | CharField | `basse`, `moyenne`, `haute` |
| `projet` | FK → Projet | Projet parent |
| `assigne_a` | FK → Utilisateur | Responsable de la tâche |

### Notification
| Champ | Type | Description |
|---|---|---|
| `utilisateur` | FK → Utilisateur | Destinataire |
| `tache` | FK → Tache | Tâche concernée |
| `message` | TextField | Contenu de la notification |
| `est_lu` | BooleanField | Statut de lecture |
| `date_creation` | DateTimeField | Date de création |

### Statistique
| Champ | Type | Description |
|---|---|---|
| `utilisateur` | FK → Utilisateur | Utilisateur évalué |
| `annee` | IntegerField | Année |
| `trimestre` | IntegerField | Trimestre (1 à 4) |
| `nb_taches_total` | IntegerField | Total des tâches assignées |
| `nb_taches_terminees_delai` | IntegerField | Tâches terminées dans les délais |
| `taux_realisation` | FloatField | Taux de complétion en % |

### Prime
| Champ | Type | Description |
|---|---|---|
| `utilisateur` | FK → Utilisateur | Bénéficiaire |
| `type_prime` | CharField | `90%` ou `100%` |
| `montant` | DecimalField | 30 000 ou 100 000 FCFA |
| `annee` | IntegerField | Année d'attribution |
| `trimestre` | IntegerField | Trimestre d'attribution |

---

## Routes API

> Toutes les routes (sauf `/api/login/` et `/api/utilisateurs/register/`) nécessitent un token JWT :  
> `Authorization: Bearer <token>`

### Authentification

| Méthode | Route | Description |
|---|---|---|
| POST | `/api/login/` | Connexion — retourne `access` et `refresh` |
| POST | `/api/token/refresh/` | Rafraîchir le token |
| POST | `/api/utilisateurs/register/` | Créer un compte |

### Utilisateurs

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/utilisateurs/` | Liste de tous les utilisateurs |
| GET | `/api/utilisateurs/profil/` | Profil de l'utilisateur connecté |
| PUT | `/api/utilisateurs/profil/update/` | Modifier son profil |
| PUT | `/api/utilisateurs/change-password/` | Changer son mot de passe |
| GET | `/api/utilisateurs/<id>/` | Détail d'un utilisateur |

### Projets

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/projets/` | Mes projets |
| POST | `/api/projets/` | Créer un projet |
| GET | `/api/projets/<id>/` | Détail d'un projet |
| PUT | `/api/projets/<id>/` | Modifier un projet |
| DELETE | `/api/projets/<id>/` | Supprimer un projet |
| GET | `/api/projets/<id>/taches/` | Tâches du projet |
| GET | `/api/projets/<id>/equipes/` | Équipes du projet |
| GET | `/api/projets/<id>/stats/` | Statistiques du projet |

### Équipes

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/equipes/` | Mes équipes |
| POST | `/api/equipes/` | Créer une équipe |
| GET | `/api/equipes/<id>/membres/` | Membres d'une équipe |
| POST | `/api/equipes/<id>/ajouter-membre/` | Ajouter un membre |
| DELETE | `/api/equipes/<id>/supprimer-membre/<user_id>/` | Retirer un membre |

### Tâches

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/taches/mes-taches/` | Mes tâches assignées |
| GET | `/api/taches/` | Toutes les tâches |
| POST | `/api/taches/` | Créer une tâche |
| PUT | `/api/taches/<id>/` | Modifier une tâche |
| DELETE | `/api/taches/<id>/` | Supprimer une tâche |
| PATCH | `/api/taches/<id>/changer-statut/` | Changer le statut |

### Notifications

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/notifications/` | Mes notifications |
| PATCH | `/api/notifications/<id>/marquer-lue/` | Marquer comme lue |
| PATCH | `/api/notifications/tout-marquer-lues/` | Tout marquer comme lu |

### Statistiques & Primes

| Méthode | Route | Description |
|---|---|---|
| GET | `/api/statistiques/` | Mes statistiques trimestrielles |
| GET | `/api/statistiques/dashboard/` | Dashboard complet (stats + primes + historique) |
| GET | `/api/statistiques/primes/` | Mes primes |
| POST | `/api/statistiques/recalculer/` | Recalculer ses stats manuellement |

---

## Logique métier

### Système de primes (enseignants uniquement)
Les primes sont calculées en fin de trimestre selon le taux de réalisation des tâches :

| Taux | Prime |
|---|---|
| 100% | 100 000 FCFA |
| ≥ 90% | 30 000 FCFA |
| < 90% | Aucune prime |

### Notifications automatiques
Une notification est créée automatiquement (+ email envoyé) quand une tâche approche de son échéance dans moins de `NOTIFICATION_DAYS_BEFORE` jours (défaut : 2 jours).

### Règles d'assignation des tâches
- Seul le créateur du projet peut créer des tâches
- L'utilisateur assigné doit être membre d'une équipe du projet
- Un étudiant ne peut pas assigner une tâche à un professeur

---

## Comptes de test

| Rôle | Email | Mot de passe |
|---|---|---|
| Professeur | stephZoux@gmail.com| zoux@26 |
| Étudiant | moussandaodevpro@gmail.com | moussa@26 |
| Étudiant | babacarSene@gmail.com | babacar@26 |


---

*Projet réalisé par Moussa NDAO — ESMT 2026*

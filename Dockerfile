# Étape 1 : Image de base
FROM python:3.11-slim AS builder

# Définir le répertoire de travail
WORKDIR /app

# Variables d'environnement pour optimiser Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Installer les dépendances système nécessaires (ex: psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Étape 2 : Image finale (production)
FROM python:3.11-slim

# Créer un utilisateur non-root pour la sécurité
RUN useradd -m -r appuser && mkdir /app && chown -R appuser /app

WORKDIR /app

# Copier les dépendances depuis le builder
COPY --from=builder /usr/local /usr/local

# Copier le code de l'application
COPY --chown=appuser:appuser . .

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Passer à l’utilisateur non-root
USER appuser

# Exposer le port
EXPOSE 8000

# Lancer l’application avec Gunicorn
CMD ["gunicorn", "gestion_tache.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3", "--threads=2"]

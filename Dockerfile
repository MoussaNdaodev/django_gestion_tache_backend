# -----------------------------
# Étape 1 : Builder
# -----------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

# Optimisation Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Installer dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Étape 2 : Image finale
# -----------------------------
FROM python:3.11-slim

WORKDIR /app

# Installer seulement les libs nécessaires à l'exécution
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Créer utilisateur non-root
RUN useradd -m -r appuser

# Copier les dépendances installées depuis builder
COPY --from=builder /usr/local /usr/local

# Copier le projet
COPY . .

# Donner les permissions
RUN chown -R appuser:appuser /app

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Passer à l'utilisateur sécurisé
USER appuser

# Exposer le port
EXPOSE 8000

# Lancer les migrations + collectstatic + gunicorn
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn gestion_tache.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --threads 2 \
    --timeout 120
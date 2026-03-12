FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m -r appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# Dockerfile — ajoute un script de démarrage
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn gestion_tache.wsgi:application --bind 0.0.0.0:8000 --workers=3"]
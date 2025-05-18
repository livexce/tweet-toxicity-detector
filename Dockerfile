# Dockerfile

# 1. Base Python
FROM python:3.9-slim

# 2. Install system dependencies (pour compiler certains packages comme blis)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. Créer un dossier de travail
WORKDIR /app

# 4. Copier les fichiers dans le conteneur
COPY . .

# 5. Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Exposer le port de l’API
EXPOSE 8000

# 7. Commande de lancement
CMD ["uvicorn", "scripts.api:app", "--host", "0.0.0.0", "--port", "8000"]

🧠 Tweet Toxicity Detector – Projet MLOps
Ce projet vise à détecter automatiquement si un tweet est toxique (1) ou non toxique (0) grâce à un pipeline MLOps complet.

🚀 Objectifs
Collecter automatiquement des tweets via API.

Nettoyer, transformer et vectoriser les textes.

Entraîner un modèle de classification binaire.

Mettre en place des tests, un lint et une CI.

Préparer le projet pour un futur déploiement.

🧠 Cadrage du projet
Données d’entrée
Type : texte brut (JSON de tweets)

Format : fichier JSON contenant des tweets

Données de sortie
Label binaire :

1 → tweet toxique

0 → tweet non toxique

Métriques d’évaluation
Accuracy

F1-score

ROC-AUC

Contraintes techniques
Latence < 200 ms par requête

Taille du modèle < 100 Mo

Budget GPU max : T4

📚 Séances du projet
🧠 Séance 1 – Initialisation du projet MLOps
Mise en place de la structure (scripts/, src/, tests/, .github/workflows)

Création de l’environnement virtuel (.venv)

Installation des outils CI : black, flake8, pytest

Configuration de GitHub Actions (CI automatique à chaque push)

🛠️ Séance 2 – Ingestion des données
Création du scraper avec API ou mock de données

Sauvegarde des tweets bruts dans data/raw/

Tests unitaires du scraper

CI intégrée avec GitHub Actions

✨ Séance 3 – Prétraitement NLP
Nettoyage des tweets

Pipeline texte avec spaCy et TfidfVectorizer

Suppression des doublons et NA

Tests unitaires des fonctions NLP

CI opérationnelle avec flake8, black, pytest

📊 Séance 4 – EDA & Split
Analyse exploratoire (EDA) dans notebooks/4_eda_featurization.ipynb

Création de features : longueur des textes, nb de mots

Split stratifié : train.csv, val.csv, test.csv

Sauvegarde dans data/processed/

🤖 Séance 5 – Entraînement & Évaluation
Pipeline TF-IDF + LogisticRegression

Entraînement sur train.csv

Évaluation sur val.csv et test.csv :

Accuracy

F1-score

Matrice de confusion

Sauvegarde du modèle dans models/toxicity_model.pkl

🔍 Séance 6 – Optimisation des hyperparamètres
Test de plusieurs modèles : RandomForestClassifier, GradientBoostingClassifier

Recherche d'hyperparamètres avec GridSearchCV et RandomizedSearchCV

Sauvegarde du meilleur modèle dans models/best_model.pkl

CI opérationnelle avec tests et linting (flake8 OK)

📈 Séance 7 – Comparaison des modèles
Évaluation de plusieurs modèles sur la même validation set

Création d’un fichier data/metrics/perf_models.csv avec les F1-scores

Visualisation via un barplot dans notebooks/7_compare_models.ipynb

🌍 Séance 8 – Déploiement API avec FastAPI
Création de l’API dans scripts/api.py avec FastAPI et Uvicorn

Route /predict pour envoyer un tweet et recevoir une prédiction (0 ou 1)

Dockerisation du projet :

Dockerfile propre

Lancement avec docker run -p 8000:8000 toxicity-api

Modèle chargé automatiquement au démarrage
⚙️ Installation
python -m venv .venv
.venv\Scripts\activate      # (Windows)
pip install -r requirements.txt

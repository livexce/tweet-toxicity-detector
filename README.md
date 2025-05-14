# 🧠 Tweet Toxicity Detector – Projet MLOps

Ce projet vise à détecter automatiquement si un tweet est toxique (`1`) ou non toxique (`0`) grâce à un pipeline MLOps complet.

## 🚀 Objectifs

- Collecter automatiquement des tweets via API.
- Nettoyer, transformer et vectoriser les textes.
- Entraîner un modèle de classification binaire.
- Mettre en place des tests, un lint et une CI.
- Préparer le projet pour un futur déploiement.
# 🧠 Cadrage du projet

## Données d’entrée

- Type : texte brut (JSON de tweets)
- Format : fichier JSON contenant des tweets

## Données de sortie

- Label binaire :
  - 1 → tweet toxique
  - 0 → tweet non toxique

## Métriques d’évaluation

- Accuracy
- F1-score
- ROC-AUC

## Contraintes techniques

- Latence < 200 ms par requête
- Taille du modèle < 100 Mo
- Budget GPU max : T4


## ⚙️ Installation

```bash
python -m venv .venv
.venv\Scripts\activate      # (Windows)
pip install -r requirements.txt

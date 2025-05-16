from pathlib import Path
import pandas as pd
import joblib
import sys

# Permet d'importer depuis src/
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from tuning import grid_search, random_search  # 👈 Import depuis src

# 📂 Chemin des données
DATA_DIR = Path("data/processed")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

# 📥 Chargement
train = pd.read_csv(DATA_DIR / "train.csv")

# 🎯 Définition des hyperparamètres
param_grid = {
    "clf__n_estimators": [50, 100],
    "clf__max_depth": [None, 10],
}

param_distributions = {
    "clf__n_estimators": [50, 100, 150],
    "clf__max_depth": [5, 10, 20, None],
}

# 🚀 Lancement des recherches
print("🔍 Lancement GridSearchCV...")
grid_result = grid_search(train["text"], train["label"], param_grid)

print("✅ Meilleurs paramètres (GridSearch) :", grid_result.best_params_)
print("✅ Score :", grid_result.best_score_)

print("\n🔍 Lancement RandomizedSearchCV...")
random_result = random_search(train["text"], train["label"], param_distributions)

print("✅ Meilleurs paramètres (RandomSearch) :", random_result.best_params_)
print("✅ Score :", random_result.best_score_)

# 💾 Sauvegarde du meilleur modèle
best_model = random_result.best_estimator_
joblib.dump(best_model, MODEL_DIR / "best_model.pkl")
print("\n📦 Modèle sauvegardé dans models/best_model.pkl")

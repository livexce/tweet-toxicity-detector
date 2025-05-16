import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

# 📂 Chemins des fichiers
DATA_DIR = Path("data/processed")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

# 📥 Chargement des données
train = pd.read_csv(DATA_DIR / "train.csv")
val = pd.read_csv(DATA_DIR / "val.csv")
test = pd.read_csv(DATA_DIR / "test.csv")

# 🧪 Pipeline avec TF-IDF + Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# 🚂 Entraînement
pipeline.fit(train["text"], train["label"])

# 📊 Évaluation sur validation
print("\n📈 Validation Report:")
y_val_pred = pipeline.predict(val["text"])
print(classification_report(val["label"], y_val_pred))
print("\nMatrice de confusion:")
print(confusion_matrix(val["label"], y_val_pred))

# 📊 Évaluation sur test
print("\n📊 Test Report:")
y_test_pred = pipeline.predict(test["text"])
print(classification_report(test["label"], y_test_pred))
print("\nMatrice de confusion:")
print(confusion_matrix(test["label"], y_test_pred))

# 💾 Sauvegarde du modèle
joblib.dump(pipeline, MODEL_DIR / "toxicity_model.pkl")
print("\n✅ Modèle sauvegardé dans models/toxicity_model.pkl")

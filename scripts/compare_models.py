import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import f1_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# 📂 Chargement des données
DATA_DIR = Path("data/processed")
train = pd.read_csv(DATA_DIR / "train.csv")
val = pd.read_csv(DATA_DIR / "val.csv")

# 🧪 Liste des modèles à tester
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "GradientBoosting": GradientBoostingClassifier(),
}

results = []

# 🔁 Boucle sur les modèles
for name, clf in models.items():
    pipe = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("clf", clf),
        ]
    )
    pipe.fit(train["text"], train["label"])
    y_pred = pipe.predict(val["text"])
    f1 = f1_score(val["label"], y_pred)
    results.append({"model": name, "f1": f1})

# 💾 Sauvegarde des scores
Path("data/metrics").mkdir(parents=True, exist_ok=True)
df = pd.DataFrame(results)
df.to_csv("data/metrics/perf_models.csv", index=False)
print("✅ Scores sauvegardés dans data/metrics/perf_models.csv")

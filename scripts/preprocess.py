import json
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from pathlib import Path


# Charger config
def load_config(path="config/preprocessing.json"):
    return json.load(open(path))


# Nettoyage
def drop_duplicates_and_na(df, text_col):
    df = df.drop_duplicates()
    df = df.dropna(subset=[text_col])
    return df


# Lemmatisation
class SpacyLemmatizer(TransformerMixin):
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return [
            " ".join([tok.lemma_ for tok in self.nlp(text) if not tok.is_stop])
            for text in X
        ]


# Pipeline NLP
def build_text_pipeline():
    return Pipeline([
        ("lemmatizer", SpacyLemmatizer()),
        ("tfidf", TfidfVectorizer(max_features=500))
    ])


def main():
    cfg = load_config()
    text_col = cfg["text"][0]

    # Lire tous les tweets JSON
    files = Path("data/raw").glob("tweet_*.json")
    df = pd.DataFrame([json.load(open(f)) for f in files])
    df = drop_duplicates_and_na(df, text_col)

    pipeline = build_text_pipeline()
    X_text = pipeline.fit_transform(df[text_col])
    print(f"✅ Pipeline NLP terminé — shape : {X_text.shape}")


if __name__ == "__main__":
    main()

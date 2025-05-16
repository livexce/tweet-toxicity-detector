# import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def add_length_features(df, col="text"):
    df["length"] = df[col].str.len()
    df["word_count"] = df[col].str.split().apply(len)
    return df


def build_tfidf(corpus, max_features=1000):
    tfidf = TfidfVectorizer(max_features=max_features, stop_words="english")
    X = tfidf.fit_transform(corpus.fillna(""))
    return X, tfidf

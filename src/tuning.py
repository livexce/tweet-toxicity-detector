from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


def build_pipeline():
    return Pipeline(
        [("tfidf", TfidfVectorizer()), ("clf", RandomForestClassifier(random_state=42))]
    )


def grid_search(X, y, param_grid, cv=3, scoring="f1", verbose=1):
    pipeline = build_pipeline()
    grid = GridSearchCV(
        pipeline,
        param_grid=param_grid,
        cv=cv,
        scoring=scoring,
        verbose=verbose,
        n_jobs=-1,
    )
    grid.fit(X, y)
    return grid


def random_search(X, y, param_distributions, cv=3, scoring="f1", n_iter=10, verbose=1):
    pipeline = build_pipeline()
    search = RandomizedSearchCV(
        pipeline,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        verbose=verbose,
        n_jobs=-1,
        random_state=42,
    )
    search.fit(X, y)
    return search

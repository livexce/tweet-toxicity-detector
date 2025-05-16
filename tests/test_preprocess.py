import pandas as pd
import pytest
import importlib.util
from scripts.preprocess import drop_duplicates_and_na


def test_drop_duplicates_and_na():
    # Vérifie si spaCy est installé sans l'importer
    if importlib.util.find_spec("spacy") is None:
        pytest.skip("spaCy not available")

    df = pd.DataFrame({"text": ["hello", "hello", None, "ok"]})
    clean = drop_duplicates_and_na(df, "text")
    assert len(clean) == 2

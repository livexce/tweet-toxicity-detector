import pytest
import pandas as pd
import importlib.util

# Vérifie si spaCy est installée
spacy_available = importlib.util.find_spec("spacy") is not None
pytestmark = pytest.mark.skipif(not spacy_available, reason="spaCy not available in CI")

from scripts.preprocess import drop_duplicates_and_na


def test_drop_duplicates_and_na():
    df = pd.DataFrame({"text": ["hello", "hello", None, "ok"]})
    clean = drop_duplicates_and_na(df, "text")
    assert len(clean) == 2

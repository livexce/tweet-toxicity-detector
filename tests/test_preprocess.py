import pytest
import pandas as pd

# Skip ce fichier dans la CI si spaCy n’est pas dispo
spacy_available = False
try:
    import spacy
    spacy_available = True
except ImportError:
    pass

pytestmark = pytest.mark.skipif(not spacy_available, reason="spaCy not available in CI")

from scripts.preprocess import drop_duplicates_and_na


def test_drop_duplicates_and_na():
    df = pd.DataFrame({"text": ["hello", "hello", None, "ok"]})
    clean = drop_duplicates_and_na(df, "text")
    assert len(clean) == 2

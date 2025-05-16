import pandas as pd
import pytest
from scripts.preprocess import drop_duplicates_and_na


def test_drop_duplicates_and_na():
    try:
        import spacy
    except ImportError:
        pytest.skip("spaCy not available in CI")

    df = pd.DataFrame({"text": ["hello", "hello", None, "ok"]})
    clean = drop_duplicates_and_na(df, "text")
    assert len(clean) == 2

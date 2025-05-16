import pandas as pd
from scripts.preprocess import drop_duplicates_and_na


def test_drop_duplicates_and_na():
    df = pd.DataFrame({
        "text": ["hello", "hello", None, "ok"]
    })
    clean = drop_duplicates_and_na(df, "text")
    assert len(clean) == 2

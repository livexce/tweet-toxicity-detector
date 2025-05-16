import pytest
import importlib.util
from scripts.preprocess import build_text_pipeline


def test_text_pipeline_outputs_matrix():
    if importlib.util.find_spec("spacy") is None:
        pytest.skip("spaCy not available in CI")

    pipe = build_text_pipeline()
    X = pipe.fit_transform(["I love pizza", "I hate spam"])
    assert hasattr(X, "toarray")

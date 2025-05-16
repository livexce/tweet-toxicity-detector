from scripts.preprocess import build_text_pipeline


def test_text_pipeline_outputs_matrix():
    pipe = build_text_pipeline()
    X = pipe.fit_transform(["I love pizza", "I hate spam"])
    assert hasattr(X, "toarray")

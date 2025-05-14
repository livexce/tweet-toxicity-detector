import os

def test_scraper_creates_files():
    files = os.listdir("data/raw")
    assert any(f.startswith("tweet_") for f in files)

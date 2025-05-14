import sqlite3
from pathlib import Path

def test_tweets_db_exists():
    db_path = Path("data/raw/tweets.db")
    assert db_path.exists()

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tweets")
    count = cursor.fetchone()[0]
    conn.close()

    assert count >= 1  # Vérifie qu’au moins un tweet est stocké

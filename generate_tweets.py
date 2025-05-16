import json
import random
from pathlib import Path

raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

toxics = [{"text": f"Ce message est toxique {i}", "label": 1} for i in range(25)]
non_toxics = [
    {"text": f"Ce message est non toxique {i}", "label": 0} for i in range(25)
]

all_tweets = toxics + non_toxics
random.shuffle(all_tweets)

file_path = raw_dir / "tweet_50.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_tweets, f, ensure_ascii=False, indent=2)

print(f"✅ Fichier généré : {file_path}")

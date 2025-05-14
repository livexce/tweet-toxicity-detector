import json
import os
from pathlib import Path


def main():
    os.makedirs("data/raw", exist_ok=True)
    # Simulation d’appel API
    sample_tweets = [
        {"text": "I hate you", "label": 1},
        {"text": "What a lovely day", "label": 0},
        {"text": "You're an idiot", "label": 1},
        {"text": "Great job on your project!", "label": 0},
    ]
    for i, tweet in enumerate(sample_tweets):
        path = Path("data/raw") / f"tweet_{i}.json"
        path.write_text(json.dumps(tweet, indent=2))
    print("4 tweets sauvegardés dans data/raw/")


if __name__ == "__main__":
    main()

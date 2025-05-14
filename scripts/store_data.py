import json
from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# Définition du modèle de données
Base = declarative_base()

class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    label = Column(Integer)

# Connexion à SQLite
engine = create_engine("sqlite:///data/raw/tweets.db")
Session = sessionmaker(bind=engine)

def store_tweets():
    Base.metadata.create_all(engine)
    session = Session()

    for file in Path("data/raw").glob("tweet_*.json"):
        with open(file, encoding="utf-8") as f:
            tweet = json.load(f)
            session.add(Tweet(text=tweet["text"], label=tweet["label"]))

    session.commit()
    session.close()
    print("✅ Tweets stockés dans data/raw/tweets.db")

if __name__ == "__main__":
    store_tweets()

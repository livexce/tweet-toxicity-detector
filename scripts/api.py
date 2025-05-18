from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# 📦 Charger modèle
model = joblib.load("models/toxicity_model.pkl")

# 📋 Créer app
app = FastAPI()

# 📥 Schéma d'entrée
class TweetInput(BaseModel):
    text: str

# 🔮 Route de prédiction
@app.post("/predict")
def predict(input: TweetInput):
    prediction = model.predict([input.text])[0]
    label = "Toxique" if prediction == 1 else "Non toxique"
    return {"label": label, "prediction": int(prediction)}

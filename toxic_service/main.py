from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()

model_checkpoint = "cointegrated/rubert-tiny-toxicity"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

device = torch.device("cpu")
model.to(device)


class TextInput(BaseModel):
    text: str


def text2toxicity(text, aggregate=True):
    """Рассчитывает токсичность текста"""
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(
            device
        )
        proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()
    if isinstance(text, str):
        proba = proba[0]
    if aggregate:
        return 1 - proba.T[0] * (1 - proba.T[-1])
    return proba


@app.post("/predict-toxicity")
async def predict_toxicity(input_data: TextInput):
    result = text2toxicity(input_data.text.lower())
    return {"toxicity_score": float(result)}


@app.get("/")
async def root():
    return {"status": "ok"}
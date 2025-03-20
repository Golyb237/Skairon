from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

# Заглушка для модели, потом заменишь на свою
def get_model_response(message, model):
    return f"Привет от {model}! Ты сказал: {message}"

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    model = data.get("model", "G1-mini-Exp")  # По умолчанию G1-mini-Exp
    reply = get_model_response(message, model)
    return {"reply": reply}

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

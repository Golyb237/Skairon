from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

def rule_based_reply(message: str) -> str:
    message = message.lower().strip()
    rules = {
        "привет": "Здравствуй! Чем могу помочь?",
        "как дела?": "Отлично, а у тебя?",
        "что умеешь?": "Пока я просто отвечаю по правилам, но скоро стану умнее!",
        "пока": "До встречи!",
    }
    return rules.get(message, "Не знаю, что ответить. Спроси что-нибудь ещё!")

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat(message: Message):
    reply = rule_based_reply(message.message)
    return {"reply": reply}
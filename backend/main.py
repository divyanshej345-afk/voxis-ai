import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

load_dotenv()

app = FastAPI(
    title="Voxis AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = []


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "app": "Voxis AI",
        "status": "running",
        "version": "1.0.0",
        "ai": "Gemini"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(data: ChatRequest):

    message = data.message.strip()

    if not message:
        return {
            "reply": "Please say something."
        }

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return {
            "reply": "Voxis AI is not connected to Gemini yet."
        }

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=message
        )

        reply = response.text

    except Exception as e:
        return {
            "reply": "Voxis AI encountered an error.",
            "error": str(e)
        }

    memory.append({
        "message": message,
        "reply": reply,
        "time": datetime.now().isoformat()
    })

    return {
        "reply": reply,
        "memory_count": len(memory)
    }


@app.get("/memory")
def get_memory():
    return {
        "memory": memory
    }

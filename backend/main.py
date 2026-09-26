from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Voxis AI")

memory = []


class UserMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "app": "Voxis AI",
        "status": "running"
    }


@app.post("/chat")
def chat(data: UserMessage):
    message = data.message.strip()

    if not message:
        return {"reply": "Please say something."}

    memory.append({
        "message": message,
        "time": datetime.now().isoformat()
    })

    return {
        "reply": f"Voxis received: {message}",
        "memory_count": len(memory)
    }


@app.get("/memory")
def get_memory():
    return {
        "memory": memory
}

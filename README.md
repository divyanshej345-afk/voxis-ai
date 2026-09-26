# Voxis AI — Voice-First Assistant MVP

A GitHub-ready MVP inspired by the Voxis AI concept:
**Speak → Understand → Execute**

## Features
- Browser voice input using Web Speech API
- AI intent extraction through an OpenAI-compatible API
- Simple memory stored in SQLite
- Safe demo actions: create a note, remember something, list memory
- React/Vite frontend
- FastAPI backend

## Run locally

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open the URL shown by Vite.

## Important
This is an MVP. Do not connect email, payments, OS controls, messaging, or other sensitive actions until authentication, authorization, confirmation flows, logging, and prompt-injection defenses are implemented.

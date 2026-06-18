# Gemini Research Chatbot

Learning-focused Streamlit + FastAPI + PostgreSQL + Gemini demo app.

## Local Development

Run the FastAPI backend:

```bash
python3 -m uvicorn backend.main:app --reload
```

Run the Streamlit frontend in another terminal:

```bash
streamlit run app.py
```

## Render Backend Deployment

This repo includes `render.yaml` for deploying the FastAPI backend to Render.

Render service settings:

- Build command: `pip install -r requirements.txt`
- Start command: `python3 -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- Health check path: `/api/health`

Set these Render environment variables:

```text
DATABASE_URL=your_neon_postgresql_connection_string
GEMINI_API_KEY=your_google_gemini_api_key
```

Do not commit database URLs or API keys to GitHub.

## Streamlit Frontend Configuration

When the FastAPI backend is deployed on Render, set the Streamlit secret:

```toml
API_BASE_URL = "https://your-render-service.onrender.com"
```

Then local Streamlit can call the deployed backend without running Uvicorn locally.

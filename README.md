# AI Research Assistant

The existing research agent and report generation flow are exposed through a FastAPI REST API and a React interface.

## Requirements

- Python 3.11 or newer
- Node.js 18 or newer
- OpenAI and Tavily API keys

Create `ai-research-assistant/.env` with the credentials expected by the existing OpenAI and Tavily integrations, for example:

```env
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

## Run the API

From the `ai-research-assistant` directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api:app --reload
```

The API listens at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

### Endpoints

- `GET /api/health` returns `{"status":"ok"}`.
- `POST /api/research` accepts `{"topic":"Your research question"}` and returns a report with `title`, `summary`, `key_findings`, `sources`, and `conclusion`.

Generated JSON reports continue to be saved in the `reports/` directory by the existing workflow.

## Run the React app

In another terminal, from `ai-research-assistant/frontend`:

```bash
npm install
npm run dev
```

Open the local URL printed by Vite (usually `http://localhost:5173`). The Vite development server proxies `/api` requests to the backend on port 8000.

Create a production frontend bundle with `npm run build`; output is written to `frontend/dist/`.

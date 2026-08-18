# FlipperComplete

FlipperComplete merges the Vue prototype frontend and FastAPI prototype backend for a motorcycle parts resale MVP.

## MVP Scope

- Track salvaged motorcycle purchases.
- Add and view parts by vehicle.
- Create marketplace listing records for parts.
- View listing status, platform, price, fees, and links.
- Run locally with SQLite for development.

## Project Layout

```
FlipperComplete/
|-- backend/   # FastAPI + SQLAlchemy + SQLite
`-- frontend/  # Vue 3 + Vite + Bootstrap
```

## Runtime Prerequisites

The backend README targets Python 3.12. This WSL environment currently has Python 3.14 without `venv`/`pip`, so dependency installation is intentionally deferred.

The frontend has Node available under NVM at `/home/bepop/.nvm/versions/node/v24.19.0`, but PATH setup needs cleanup before normal `npm` commands work in non-interactive shells.

## Run Backend

```bash
cd /home/bepop/Workspace/FlipperComplete/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --app-dir src --reload --host 0.0.0.0 --port 8080
```

API docs: http://localhost:8080/flipper/swagger

## Run Frontend

```bash
cd /home/bepop/Workspace/FlipperComplete/frontend
npm install
npm run dev -- --host 0.0.0.0
```

Frontend defaults to `http://localhost:8080` for API calls. Override with `VITE_API_BASE_URL` if needed.

## MVP Notes

The prototype currently treats fields ending in `_c` as dollar amounts in the UI/API. That should be normalized before production accounting work.

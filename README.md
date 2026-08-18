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


## What Changed During Merge

This repo is more than a file move from the two prototypes. The initial merge also made light integration fixes so the frontend and backend are easier to run together for MVP work.

- Created a unified repo structure with `frontend/` for Vue and `backend/` for FastAPI.
- Added `frontend/src/api.js` so the frontend API base URL can be configured with `VITE_API_BASE_URL`.
- Replaced hard-coded frontend API calls to `http://localhost:8080/...` with the shared API URL helper.
- Fixed the listing platform typo/mismatch from `MAKRETPLACE` to `FACEBOOK`.
- Stopped transforming listing platform values with `toUpperCase()` so submitted values stay aligned with supported backend values.
- Added MVP default statuses in forms such as `PURCHASED`, `IN_BIN`, and `DRAFT`.
- Fixed parts query URL building when filtering by `vehicle_id`.
- Updated backend database setup so tables are created through `init_db()` at app startup.
- Updated the FastAPI entrypoint so `app = init_app()` is available for `uvicorn api.main:app`.
- Cleaned API metadata tag definitions for Swagger/OpenAPI grouping.
- Added root-level run documentation and `.env.example` files for both frontend and backend.

This was not a full production refactor. Dependency installation and full app runtime verification were intentionally deferred.

## MVP Notes

The prototype currently treats fields ending in `_c` as dollar amounts in the UI/API. That should be normalized before production accounting work.

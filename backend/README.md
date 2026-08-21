# Motorcycle Parts Resale Platform

## 🚀 Summary
This project is part of a business venture to purchase salvaged motorcycles, dismantle them, and sell their parts across multiple online platforms. By integrating auctions, structured disassembly, smart inventory tracking, and dynamic platform support (eBay, Facebook, etc.), the system aims to maximize part resale profit and streamline operations.

Built using FastAPI and SQLAlchemy with a modular design to support expansion into multiple sales channels.

## 📦 Features
- Track motorcycle purchases and parts inventory
- Estimate resale value per part
- Calculate ROI by vehicle and platform
- Cross-list parts across eBay, Facebook, Shopify, and more
- Custom barcode and locker/bin labeling support
- Dashboard for part status, profit, and sales insights

## 🛠 Tech Stack
- Python 3.12 (via `pyenv`)
- FastAPI + SQLAlchemy 2.0
- SQLite (dev) / MariaDB (prod-ready)
- Pydantic v2
- Celery + Redis (for background syncing)
- eBay SDK (with pluggable interface for others)

## 📥 Setup Instructions

### 1. Install Python 3.12 with `pyenv`
```bash
pyenv install 3.12.11
```

If installation prints a warning that `_tkinter` was not compiled, the Python
installation can still be used by this backend. Tkinter is an optional desktop
GUI dependency and is not required by FastAPI.

If pyenv says the version already exists, confirm the installation directly:

```bash
~/.pyenv/versions/3.12.11/bin/python --version
```

It should print `Python 3.12.11`.

### 2. Initialize pyenv in Bash

The pyenv shims must be present on `PATH` for the `python` command to use the
selected pyenv version. Add pyenv initialization to `~/.bashrc` once:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null && eval "$(pyenv init - bash)"' >> ~/.bashrc
exec bash
```

Select Python 3.12 for this backend and verify it:

```bash
cd /home/bepop/Workspace/FlipperComplete/backend
pyenv local 3.12.11
pyenv rehash
python --version
```

The output should be `Python 3.12.11`. A pyenv local version applies only in
this directory and its children. To select Python 3.12 globally instead, run
`pyenv global 3.12.11`.

### 3. Create and activate the virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

If `.venv` was previously created with Python 3.14, preserve it and create a
new Python 3.12 environment:

```bash
mv .venv .venv-python314
python -m venv .venv
source .venv/bin/activate
```

Confirm that the active environment is correct with `python --version`.

### 4. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The application initializes its SQLite tables during startup, so a separate
schema-import command is not required.

### 5. Run the application
```bash
python -m uvicorn api.main:app --app-dir src --reload --host 0.0.0.0 --port 8080
```

The entry point is `src/api/main.py`; this repository does not contain an
`app.main` module. API documentation is available at
http://localhost:8080/flipper/swagger after startup.

If Python reports the SQLAlchemy `TypingOnly` assertion while starting the
application, check `python --version`. That error occurs when the pinned
SQLAlchemy 2.0.29 package is run with Python 3.14; recreate `.venv` with Python
3.12 as described above.

## ⚙️ Project Structure (Initial)
```
├── src/
│   ├── api/
│   │   ├── main.py      # FastAPI entry point
│   │   ├── vehicles.py  # Vehicle routes
│   │   ├── parts.py     # Part routes
│   │   └── listings.py  # Listing routes
│   └── database.py      # SQLAlchemy models and database setup
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🔜 Coming Soon
- Marketplace webhook syncing
- Admin UI
- Auto-pricing tools based on eBay sold data
- Locker label printing and QR part lookup

---

_Developed by Kevin Hernandez – Fullstack Python Engineer & Founder_

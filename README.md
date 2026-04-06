# JobFlow
ETL pipeline for job market analytics (HH and other sources).

This is a pet project to sharpen my data engineering skills by building a practical end-to-end pipeline from scratch.

## Goals
- Collect job vacancies via official APIs
- Store raw data and build a normalized layer
- Run basic analytics on skills, salaries, and geography
- Keep the project simple, reproducible, and easy to extend

## Scope (MVP)
- Source: HH API (more sources later)
- Stack: Python, PostgreSQL, Docker Compose, requests, pandas
- Layers: `extract` → `transform` → `load`

## Architecture
- `app/extract` — API clients and data fetching
- `app/transform` — normalization, parsing, and enrichment
- `app/load` — database writes and upserts
- `app/db` — connection and schema init
- `app/analytics` — aggregate queries and reporting
- `app/api` — API layer (optional, later)

## Quick Start
1. Create and activate venv
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Start PostgreSQL
```bash
docker compose up -d
```
4. Initialize DB
```bash
python3 -m app.db.init_db
```
5. Run first load
```bash
python3 -m app.main
```

## Roadmap
- Add normalized layer (salary, city, employer, published_at, skills)
- Add basic analytics (top skills, median salary, demand by role)
- Add scheduling (Airflow or cron)
- Add API endpoints (FastAPI)

## Notes
- This project uses only official/public APIs and avoids scraping.

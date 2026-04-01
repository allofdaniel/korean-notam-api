# API Reference

The repository includes a small FastAPI reference server in [`reference_api/main.py`](/mnt/c/Users/allof/korean-notam-api/reference_api/main.py).

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn reference_api.main:app --reload
```

## Endpoints

### `GET /health`

Returns API liveness and the current data backend mode.

### `GET /api/v1/notams`

List NOTAM records.

Query parameters:

- `location`: optional ICAO filter
- `query`: optional free-text match against `notam_no`, `qcode`, or text
- `limit`: default `100`, max `500`

### `GET /api/v1/notams/{location}`

List records for a single location.

### `GET /api/v1/notams/{location}/{notam_no}`

Get one NOTAM record.

Example:

```bash
curl 'http://127.0.0.1:8000/api/v1/notams/RKSI/A0001%2F26'
```

## Backends

The reference API uses:

- SQLite from `NOTAM_SQLITE_PATH` when provided and readable
- otherwise the synthetic fixture in [`examples/sample_notams.json`](/mnt/c/Users/allof/korean-notam-api/examples/sample_notams.json)

This keeps the reference server runnable without shipping operational data.

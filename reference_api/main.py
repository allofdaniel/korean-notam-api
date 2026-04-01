from __future__ import annotations

import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_SAMPLE_PATH = ROOT_DIR / "examples" / "sample_notams.json"


def parse_timestamp(value: Any) -> str | None:
    if value is None:
        return None

    text = str(value).strip()
    if not text:
        return None

    digits = "".join(ch for ch in text if ch.isdigit())

    if len(digits) == 10:
        dt = datetime(
            2000 + int(digits[0:2]),
            int(digits[2:4]),
            int(digits[4:6]),
            int(digits[6:8]),
            int(digits[8:10]),
            tzinfo=timezone.utc,
        )
        return dt.isoformat().replace("+00:00", "Z")

    if len(digits) == 12:
        dt = datetime(
            int(digits[0:4]),
            int(digits[4:6]),
            int(digits[6:8]),
            int(digits[8:10]),
            int(digits[10:12]),
            tzinfo=timezone.utc,
        )
        return dt.isoformat().replace("+00:00", "Z")

    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return text

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def is_active(end_time: str | None) -> bool:
    if not end_time:
        return True

    try:
        end_dt = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
    except ValueError:
        return True

    return end_dt >= datetime.now(timezone.utc)


def normalize_record(record: dict[str, Any], source: str) -> dict[str, Any]:
    normalized = {
        "notam_no": str(record.get("notam_no") or record.get("notam_number") or "").strip(),
        "location": str(record.get("location") or record.get("a_location") or "").strip().upper(),
        "notam_type": str(record.get("notam_type") or record.get("series_type") or "").strip(),
        "qcode": str(record.get("qcode") or record.get("q_code") or "").strip(),
        "issue_time": parse_timestamp(record.get("issue_time")),
        "start_time": parse_timestamp(record.get("start_time") or record.get("b_start_time")),
        "end_time": parse_timestamp(record.get("end_time") or record.get("c_end_time")),
        "full_text": str(record.get("full_text") or record.get("e_text") or "").strip(),
        "full_text_detail": str(record.get("full_text_detail") or record.get("full_text") or "").strip(),
        "source": source,
    }
    normalized["is_active"] = is_active(normalized["end_time"])
    return normalized


def load_sample_records(sample_path: Path = DEFAULT_SAMPLE_PATH) -> list[dict[str, Any]]:
    payload = json.loads(sample_path.read_text(encoding="utf-8"))
    return [normalize_record(item, source="sample") for item in payload]


def load_sqlite_records(db_path: Path) -> list[dict[str, Any]]:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    try:
        rows = connection.execute(
            """
            SELECT
                notam_no,
                location,
                notam_type,
                qcode,
                issue_time,
                start_time,
                end_time,
                full_text,
                full_text_detail
            FROM notam_records
            ORDER BY issue_time DESC
            """
        ).fetchall()
    finally:
        connection.close()

    return [normalize_record(dict(row), source="sqlite") for row in rows]


def load_records() -> tuple[list[dict[str, Any]], str]:
    sqlite_path = os.getenv("NOTAM_SQLITE_PATH")

    if sqlite_path:
        db_path = Path(sqlite_path)
        if db_path.exists():
            return load_sqlite_records(db_path), "sqlite"

    return load_sample_records(), "sample"


def filter_records(
    records: list[dict[str, Any]],
    location: str | None,
    query: str | None,
    limit: int,
) -> list[dict[str, Any]]:
    filtered = records

    if location:
        wanted = location.strip().upper()
        filtered = [record for record in filtered if record["location"] == wanted]

    if query:
        needle = query.strip().lower()
        filtered = [
            record
            for record in filtered
            if needle in record["notam_no"].lower()
            or needle in record["qcode"].lower()
            or needle in record["full_text"].lower()
            or needle in record["full_text_detail"].lower()
        ]

    return filtered[:limit]


app = FastAPI(
    title="Korean NOTAM API",
    version="0.1.0",
    description="Reference API for Korean NOTAM collection and monitoring workflows.",
)


@app.get("/")
def root() -> dict[str, Any]:
    _, backend = load_records()
    return {
        "name": "Korean NOTAM API",
        "backend": backend,
        "docs_url": "/docs",
        "endpoints": [
            "/health",
            "/api/v1/notams",
            "/api/v1/notams/{location}",
            "/api/v1/notams/{location}/{notam_no}",
        ],
    }


@app.get("/health")
def health() -> dict[str, Any]:
    _, backend = load_records()
    return {"status": "ok", "backend": backend}


@app.get("/api/v1/notams")
def list_notams(
    location: str | None = Query(default=None),
    query: str | None = Query(default=None),
    limit: int = Query(default=100, ge=1, le=500),
) -> dict[str, Any]:
    records, backend = load_records()
    filtered = filter_records(records, location=location, query=query, limit=limit)
    return {
        "data": filtered,
        "count": len(filtered),
        "backend": backend,
        "query": {"location": location, "query": query, "limit": limit},
    }


@app.get("/api/v1/notams/{location}")
def list_notams_for_location(
    location: str,
    limit: int = Query(default=100, ge=1, le=500),
) -> dict[str, Any]:
    records, backend = load_records()
    filtered = filter_records(records, location=location, query=None, limit=limit)
    return {
        "location": location.upper(),
        "data": filtered,
        "count": len(filtered),
        "backend": backend,
    }


@app.get("/api/v1/notams/{location}/{notam_no:path}")
def get_notam(location: str, notam_no: str) -> dict[str, Any]:
    records, backend = load_records()
    wanted_location = location.upper()
    wanted_notam = notam_no.strip().upper()

    for record in records:
        if record["location"] == wanted_location and record["notam_no"].upper() == wanted_notam:
            return {"data": record, "backend": backend}

    raise HTTPException(status_code=404, detail="NOTAM not found")

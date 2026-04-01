# Korean NOTAM API and Crawler

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

[![CI](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml/badge.svg)](https://github.com/allofdaniel/korean-notam-api/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Open-source Python tooling for collecting, normalizing, monitoring, and self-hosting Korean NOTAM data.

Korea does not currently offer an easy public developer-facing NOTAM API. This repository packages the reusable core that downstream teams need: collection, normalization, local persistence, change detection, and a small FastAPI reference API.

## What You Get

- direct collection from Korea AIM NOTAM endpoints
- optional Selenium fallback for brittle upstream flows
- normalized JSON records for downstream automation
- SQLite persistence and change detection workflows
- self-hostable FastAPI reference API
- sample fixture and tests for local integration work

## Quick Start

### 1. Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### 2. Run the reference API

```bash
python3 -m uvicorn reference_api.main:app --reload
```

Open:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/api/v1/notams`

### 3. Query sample NOTAM data

```bash
curl "http://127.0.0.1:8000/api/v1/notams/RKSI"
```

Example response:

```json
{
  "location": "RKSI",
  "count": 1,
  "backend": "sample",
  "data": [
    {
      "notam_no": "A0001/26",
      "location": "RKSI",
      "qcode": "QMRLC",
      "is_active": true,
      "full_text": "RWY inspection in progress"
    }
  ]
}
```

## Why This Repository Exists

Korean NOTAM access is still awkward for independent developers, researchers, and small product teams. This project exists to reduce repeated scraping, parsing, and normalization work so other teams can build aviation workflows faster on top of reusable infrastructure.

## Who This Helps

- aviation research and education projects
- flight-planning and dispatch prototypes
- drone and UAM briefing tools
- airport operations dashboards
- teams that need normalized Korean aviation notices in a self-hosted stack

## Main Entry Points

- `notam_crawler_api.py`: direct collection path
- `notam_hybrid_crawler.py`: direct collection plus Selenium fallback
- `notam_monitor.py`: monitoring workflow for repeated checks
- `notam_change_detector.py`: change detection helpers
- `reference_api/main.py`: FastAPI reference implementation
- `examples/sample_notams.json`: local fixture for tests and demos

## Project Status

This is active infrastructure software, not a polished SDK.

- the direct crawler is the main path
- the Selenium crawler is a fallback path
- the reference API is intended as a practical integration surface
- hosted or commercial delivery can sit on top of the same open-source core

## Additional Commands

Run the direct crawler:

```bash
python3 notam_crawler_api.py
```

Run the hybrid crawler:

```bash
python3 -m pip install -r requirements-selenium.txt
python3 notam_hybrid_crawler.py
```

Run the monitor workflow:

```bash
python3 notam_monitor.py
```

Run tests:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

## Documentation

- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)
- [Ecosystem Impact](docs/ecosystem-impact.md)
- [Roadmap](docs/roadmap.md)
- [Source And Safety Notes](docs/source-and-safety.md)
- [Use Cases](docs/use-cases.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)

## Managed Service Direction

A separate hosted landing page exists here:

- https://notam-api-landing.vercel.app/

The hosted direction does not replace the open-source repository. The OSS value is in the collector, parser, schema, and self-hostable building blocks.

## Important Notes

- this is not an official government API
- upstream source systems and response formats can change
- fetched NOTAM data may still be subject to the original source system's terms
- do not use this repository as the sole source for operational flight briefing or safety-critical decision making

## Contributing

Contributions are welcome, especially around:

- parser accuracy
- API contract design
- documentation
- better tests
- Korean aviation data validation

Please read [Contributing](CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md), and [Source And Safety Notes](docs/source-and-safety.md) before opening issues or pull requests.

## License

MIT. See [LICENSE](LICENSE).

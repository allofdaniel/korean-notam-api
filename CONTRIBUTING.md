# Contributing

Issues and pull requests are welcome.

Before contributing, read:

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Source And Safety Notes](docs/source-and-safety.md)

## Good First Contributions

- improve parsing reliability
- document response fields
- add smoke tests
- improve Korean/English documentation
- add examples for downstream API usage

## Before Opening A PR

- use the GitHub issue and PR templates when they fit
- keep secrets and deployment credentials out of the repository
- prefer synthetic samples over real operational dumps
- avoid adding large generated files
- document behavior changes in the README or docs when relevant
- call out any source-system or safety implications explicitly

## Development Notes

- `notam_crawler_api.py` is the primary collector path
- `notam_crawler.py` is the Selenium fallback
- `notam_monitor.py` ties crawling and change detection together

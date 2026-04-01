import json
from pathlib import Path

from reference_api.main import normalize_record


def test_sample_fixture_has_required_fields() -> None:
    fixture_path = Path("examples/sample_notams.json")
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))

    assert isinstance(payload, list)
    assert payload

    for item in payload:
        normalized = normalize_record(item, source="sample")
        assert normalized["notam_no"]
        assert normalized["location"]
        assert normalized["notam_type"]

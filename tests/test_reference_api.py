from fastapi.testclient import TestClient

from reference_api.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_notams_returns_fixture_data() -> None:
    response = client.get("/api/v1/notams")
    payload = response.json()

    assert response.status_code == 200
    assert payload["count"] >= 2
    assert payload["backend"] == "sample"
    assert payload["data"][0]["notam_no"]


def test_location_filter_works() -> None:
    response = client.get("/api/v1/notams/RKSI")
    payload = response.json()

    assert response.status_code == 200
    assert payload["count"] == 1
    assert payload["data"][0]["location"] == "RKSI"


def test_detail_endpoint_supports_notam_number_with_slash() -> None:
    response = client.get("/api/v1/notams/RKSI/A0001%2F26")
    payload = response.json()

    assert response.status_code == 200
    assert payload["data"]["notam_no"] == "A0001/26"

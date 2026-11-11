from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_valid_trip_request():
    payload = {
        "origin": "Kuala Lumpur",
        "destinations": ["Tokyo", "Osaka"],
        "start_date": "2027-03-10",
        "end_date": "2027-03-16",
        "budget": "5000.00",
        "currency": "MYR",
        "travelers": 2,
        "interests": ["anime", "food"],
        "travel_style": "relaxed",
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["valid"] is True
    assert data["trip"]["destinations"] == ["Tokyo", "Osaka"]
    assert data["trip"]["budget"] == "5000.00"
    assert data["trip"]["travelers"] == 2


def test_empty_destinations():
    payload = {
        "destinations": [],
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 422


def test_negative_budget():
    payload = {
        "destinations": ["Tokyo"],
        "budget": -500,
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 422


def test_invalid_travelers():
    payload = {
        "destinations": ["Tokyo"],
        "travelers": 0,
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 422


def test_end_date_before_start_date():
    payload = {
        "destinations": ["Tokyo"],
        "start_date": "2027-03-20",
        "end_date": "2027-03-10",
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 422


def test_optional_fields():
    payload = {
        "destinations": ["Tokyo"],
    }

    response = client.post(
        "/api/v1/trips/validate",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["trip"]["origin"] is None
    assert data["trip"]["budget"] is None
    assert data["trip"]["travelers"] == 1

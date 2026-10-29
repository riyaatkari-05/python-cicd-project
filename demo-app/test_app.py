from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Jenkins CI/CD deployment successful!" in response.data


def test_positive_number():
    client = app.test_client()
    response = client.get("/check/10")

    assert response.status_code == 200
    assert response.json["result"] == "Positive"


def test_negative_number():
    client = app.test_client()
    response = client.get("/check/-5")

    assert response.status_code == 200
    assert response.json["result"] == "Negative"


def test_zero():
    client = app.test_client()
    response = client.get("/check/0")

    assert response.json["result"] == "Zero"
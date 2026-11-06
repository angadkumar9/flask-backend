from app import app


def test_health():
    r = app.test_client().get("/api/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_message():
    r = app.test_client().get("/api/message")
    assert r.status_code == 200
    assert "Flask" in r.get_json()["message"]

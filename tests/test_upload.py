import re
from fastapi.testclient import TestClient


def test_upload(client: TestClient):
    with open("tests/testing.jpg", "rb") as f:
        response = client.post("/upload/", files={"file": ("test.jpg", f, "image/jpeg")})
    assert response.status_code == 200

    pattern = r"^.*\.jpg$"
    assert re.match(pattern, response.json()["filename"])

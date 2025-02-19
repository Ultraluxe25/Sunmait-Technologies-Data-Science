import pytest
from fastapi.testclient import TestClient
from predict import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "200 OK"}
    print("test_ping OK")

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the sentiment analysis API!"}
    print("test_root OK")

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert response.json()["sentiment"]["label"] in ["POSITIVE", "NEGATIVE"]
    print("test_predict_positive OK")

def test_predict_negative():
    response = client.post("/predict", json={"text": "I hate this product!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert response.json()["sentiment"]["label"] in ["POSITIVE", "NEGATIVE"]
    print("test_predict_negative OK")

def test_predict_invalid_input():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert response.json()["sentiment"]["label"] in ["POSITIVE", "NEGATIVE"]
    print("test_predict_invalid_input OK")


if __name__ == "__main__":
    pytest.main()
    
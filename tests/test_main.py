import copy
from fastapi.testclient import TestClient
from main import app


mock_character_1 = {
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1998
    }

mock_character_2 = {
        "name": "Yoda",
        "height": 60,
        "mass": 20,
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": 1990
    }

def test_root(test_client):
    response = test_client.get("/api/v1/character/getAll")
    assert response.status_code == 200
    data = response.json()
    assert data["items"] == []

def test_add_character_one(test_client):
    response = test_client.post("/api/v1/character/add", json=mock_character_1)
    assert response.status_code == 200
    data = response.json()
    assert data == dict(mock_character_1, **{"id": 1})

def test_add_character_empty_height(test_client):
    payload = copy.deepcopy(mock_character_1)
    payload["height"] = None
    response = test_client.post("/api/v1/character/add", json=payload)
    data = response.json()
    assert response.status_code == 422
    assert data["detail"][0]["msg"] == 'Input should be a valid integer'

def test_add_character_empty_name(test_client):
    payload = copy.deepcopy(mock_character_1)
    payload["name"] = ""
    response = test_client.post("/api/v1/character/add", json=payload)
    data = response.json()
    assert response.status_code == 422
    assert data["detail"][0]["msg"] == 'String should have at least 1 character'

def test_get_character(test_client):
    character_id_to_retreive = 1
    response = test_client.get(f"/api/v1/character/get/{character_id_to_retreive}")
    assert response.status_code == 200
    data = response.json()
    assert data == dict(mock_character_1, **{"id": 1})

def test_add_character_two(test_client):
    response = test_client.post("/api/v1/character/add", json=mock_character_2)
    assert response.status_code == 200
    data = response.json()
    assert data == dict(mock_character_2, **{"id": 2})

def test_delete_character(test_client):
    character_id_to_delete = 2
    response = test_client.delete(f"/api/v1/character/delete/{character_id_to_delete}")
    assert response.status_code == 200
    data = response.json()
    assert data == {'message': "character 2 (Yoda) deleted successfully"}

def test_delete_unexistend_character(test_client):
    character_id_to_delete = 3
    response = test_client.delete(f"/api/v1/character/delete/{character_id_to_delete}")
    assert response.status_code == 404
    data = response.json()
    assert data == {'message': f"Character with id {character_id_to_delete} doesn't exist"}
import pytest
from ml.app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_query(client):
    response = client.post('/query/', json={
        "theme": "Shiny sun brights through the forest"
    })
    assert response.status_code == 200
    response_json = response.get_json()
    assert "response" in response_json

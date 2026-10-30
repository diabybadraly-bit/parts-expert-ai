import pytest
from app import app, init_db, DB_PATH
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_search(client):
    rv = client.get('/api/search?q=Filtre')
    assert rv.status_code == 200
    data = rv.get_json()
    assert len(data) > 0
    assert data[0][1] == "FLT-001"

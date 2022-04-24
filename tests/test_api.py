import json
from app import app


def test_index_route():
    response = app.test_client().get('/')
    results = json.loads(response.data.decode('utf-8')).get("results")
    assert response.status_code == 200
    assert type(results) is dict
    assert results['message'] == "App is Live!"
    assert results['status'] == 200


def test_show_data_route():
    response = app.test_client().get('/show_data')
    results = json.loads(response.data.decode('utf-8')).get("results")
    assert response.status_code == 200
    assert type(results) is dict
    assert type(results['data']) is list
    assert len(results['data']) == 25
    assert type(results['message']) is str
    assert results['message'] ==  "Showing 25 rows" 
    assert type(results['status']) is int
    assert type(results['page']) is int
    assert type(results['total_pages']) is int
    assert results['status'] == 200

def test_show_data_with_pagination_route():
    page = 2
    url = f'/show_data/{page}'
    response = app.test_client().get(url)
    results = json.loads(response.data.decode('utf-8')).get("results")
    assert response.status_code == 200
    assert type(results) is dict
    assert type(results['data']) is list
    assert len(results['data']) == 25
    assert type(results['message']) is str
    assert results['message'] ==  "Showing 25 rows" 
    assert type(results['status']) is int
    assert type(results['page']) is int
    assert type(results['total_pages']) is int
    assert results['status'] == 200

    
def test_load_data_route():
    response = app.test_client().get('/load_data')
    results = json.loads(response.data.decode('utf-8')).get("results")
    assert response.status_code == 200
    assert type(results) is dict
    assert type(results['message']) is str
    assert results['status'] == 200
    assert "New data pulled" in results['message']
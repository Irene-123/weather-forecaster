"""
test_app.py - API Test Cases WITHOUT conftest.py
All fixtures defined in this file

This shows how to write tests WITHOUT a separate conftest.py file.
"""

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


"""
When you write:
    def test_something(client):
        
pytest sees 'client' in the function parameters and:
1. Looks for a fixture named 'client'
2. Calls that fixture function
3. Takes the returned value (the test client)
4. Passes it as the 'client' parameter to your test

You DON'T call it manually! pytest does it automatically.

Example:
    def test_get_users(client):  # <- pytest passes client here
        response = client.get('/users')  # <- use it like normal variable
"""


def test_get_users(client):
    response = client.get('/users')

    assert response.status_code == 200

    data = response.get_json()
    
    assert len(data) == 4
    assert "Alice" in data
    assert "Bob" in data



def test_user_not_found(client):
    """Test GET /users/999 (non-existent user)"""
    response = client.get('/users/999')
    
    assert response.status_code == 404
    
    data = response.get_json()
    assert "error" in data





@pytest.mark.parametrize("user_id,expected_name", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
    (4, "Diana"),
])
def test_multiple_users(client, user_id, expected_name):
    """
    Test all users with one test function
    
    Note: Both 'client' and 'user_id', 'expected_name' are passed:
    - client: from the fixture
    - user_id, expected_name: from parametrize
    """
    response = client.get(f'/users/{user_id}')
    
    data = response.get_json()
    assert data["name"] == expected_name




def test_response_is_json(client):
    """Test that response is JSON format"""
    response = client.get('/users')
    
    assert response.content_type == 'application/json'



def test_all_users_in_list(client):
    """Test that all 4 users are in the list"""
    response = client.get('/users')
    
    data = response.get_json()
    
    expected_users = ["Alice", "Bob", "Charlie", "Diana"]
    assert data == expected_users



def test_user_has_all_fields(client):
    """
    Test that user object has all required fields
    
    'client' here is the test client from the fixture above.
    You use it just like a regular variable!
    """
    response = client.get('/users/1')
    
    data = response.get_json()
    
    # Check all required fields exist
    assert "name" in data
    assert "age" in data
    assert "role" in data
    assert "department" in data
    assert "email" in data



def test_user_field_types(client):
    """Test that user fields have correct data types"""
    response = client.get('/users/1')
    
    data = response.get_json()
    
    assert isinstance(data["name"], str)
    assert isinstance(data["age"], int)
    assert isinstance(data["role"], str)
    assert isinstance(data["department"], str)
    assert isinstance(data["email"], str)


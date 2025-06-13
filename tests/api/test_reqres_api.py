import pytest
from src.api_clients.reqres_client import ReqresClient


@pytest.mark.api
def test_get_users_list():
    # Arrange
    client = ReqresClient()

    # Act
    response = client.get_users(page=2)

    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['page'] == 2
    assert isinstance(response_data['data'], list)
    assert len(response_data['data']) > 0 
from unittest.mock import Mock, patch

import pytest

from src.services.auth import auth_service


def test_get_todos(client, get_token):
    with patch.object(auth_service, 'cache') as redis_mock:
        redis_mock.get.return_value = None
        token = get_token
        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("api/todos", headers=headers)
        assert response.status_code == 200, response.text
        data = response.json()
        assert len(data) == 0


def test_create_todo(client, get_token, monkeypatch):
    with patch.object(auth_service, 'cache') as redis_mock:
        redis_mock.get.return_value = None
        token = get_token
        headers = {"Authorization": f"Bearer {token}"}
        response = client.post("api/todos", headers=headers, json={
            "title": "test",
            "description": "test",
        })
        assert response.status_code == 201, response.text
        data = response.json()
        assert "id" in data
        assert data["title"] == "test"
        assert data["description"] == "test"

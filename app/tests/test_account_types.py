import json
import pytest

from app.cruds import account_type


def test_create_account_type_success(test_app, monkeypatch):
    request_payload = {"name": "checking"}
    response_payload = {"id": 1, "name": "checking"}

    def mock_create_account_type(**kwargs):
        return response_payload

    monkeypatch.setattr(account_type, "create_account_type", mock_create_account_type)

    response = test_app.post("/account_types/", data=json.dumps(request_payload))

    assert response.status_code == 201
    assert response.json() == response_payload
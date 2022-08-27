from API.main import app
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket


# def test_websocket():
#     with client.websocket_connect("http://127.0.0.1:8000/teste/sendDocuments") as  websocket:
#         data = websocket.receive_json()
#         assert ==

def test_read_main():
    with TestClient(app) as client:
        params = {"endpoint": "http://127.0.0.1:8000/teste/sendDocuments",
                  "request_method": "POST",
                  "request_body": {"OUTROTESTE": "OTHER DICT"},
                  "type_org": "Santander"}

        response = client.post("http://127.0.0.1:8000/teste/sendDocuments", json=params)
        assert response.status_code == 200
        assert response.json() == params




def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 100
    assert response.data.decode("utf-8") == "Hello, world!"

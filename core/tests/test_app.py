from flask import Flask

url = 'http://127.0.0.5000'

def test_app(app):
    assert isinstance(app, Flask)

def test_render_main(client):
    results = client.get(url+'/')
    assert results.status_code == 200


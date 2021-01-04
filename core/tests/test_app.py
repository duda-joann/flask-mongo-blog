from flask import Flask

url = 'http://127.0.0.5000'


def test_app(app):
    assert isinstance(app, Flask)


def test_render_main(client):
    results = client.get(url+'/')
    assert results.status_code == 200


def test_posts_lists(client):
    results = client.get(url+'/posts/list/')
    assert results.status_code == 200


def test_posts_by_tag(client):
    results = client.get(url + '/posts/1/')
    assert results.status_code == 200


def test_create_new_post(client):
    results = client.get(url+ '/create-new-post/')
    assert results.status_code == 200


def test_update_post(client):
    results = client.get(url+'update-post/')
    assert results.status_code == 200


def test_delete_post(client):
    results = client.get(url + '/delete-post/1')
    assert results.status_code == 200


def test_register_user(client):
    results = client.get(url + '/user/registered')
    assert results.status_code == 200


def test_signout(client):
    results = client.get(url + '/user/signout/')
    assert results.status_code == 200


def test_login(client):
    results = client.get(url + '/user/login')
    assert results.status_code == 200


def test_generate_dashboard(client):
    results = client.get(url + '/dashboard/')
    assert results.status_code == 200



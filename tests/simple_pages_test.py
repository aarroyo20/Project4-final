"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data



def test_request_register(client):
    """This makes the register page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data

def test_request_login(client):
    """This makes the login page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data



def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
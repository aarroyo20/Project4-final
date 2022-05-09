from app import User


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_register_user(client, application):
    """This tests to see if user can register"""
    response = client.post('/register', data={
        'email': 'ara55@njit.edu',
        'password': '123456',
        'confirm': '123456'
    }, follow_redirects=True)
    assert response.status_code == 200
    user = User.query.filter_by(email='ara55@njit.edu').first()
    assert user is not None
    assert user.email == 'ara55@njit.edu'

def test_user_login_post_registration(client):
    """This tests to see if user can login after registering"""
    data = {
        'email' : 'ara55@njit.edu',
        'password' : 'password'
    }
    resp = client.post('login', follow_redirects=True, data=data)
    assert resp.status_code == 200


def user_dashboard_access_deny(client):
    """testing user access to dashboard"""
    response = client.get("/dashboard")
    assert response.status_code == 403
    return client.get('/dashboard', follow_redirects=False)

def test_deny_access_dashboard_page_without_login(client):
    """Testing user access to dashboard"""
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    html = response.get_data(as_text=True)
    assert 'Please log in to access this page.' in html

def test_user_logout(client, application):
    """This tests user logging out"""
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Login</h2>" in response.data


def test_logout(client, application):
    """error page test"""
    # pylint: disable=unused-argument,redefined-outer-name
    resp = client.get('/logout')
    # if user is logged in, redirect to index
    assert resp.status_code == 302



def test_user_logout_fail_without_register(client, application):
    """Tests users logging out without logging in"""
    response = client.post('/logout', data={
        'email': 'ara55@njit.edu',
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=False)
    assert response.status_code == 405


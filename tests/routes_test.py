"""This test the homepage"""
from flask import Flask
import json
import logging
from app.auth import browse_users
from app import db
import os
from app import config
import logs
from app.db import config
from pathlib import Path

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_user_user_profile(client, application):
    """Tests profile edits for user"""
    response = client.post('/profile', data={
        'email': 'ara55@njit.edu',
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_user_manage_account(client, application):
    """"Tests user editing/managing their user account"""
    response = client.post('/account', data={
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_user_user_management(client):
    """"Tests user editing/managing their user account"""
    response = client.get('/users', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    html = response.get_data(as_text=True)
    assert '<h2>Login</h2>' in html

def test_file_uploads(application, client):
    """Tests the upload"""
    root = config.Config.BASE_DIR
    filepath = root + '/..app/uploads/'
    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder)
    assert os.path.exists(file_upload) == True

def test_get_transaction_route(client):
    """Transactions test """
    response = client.get("/transactions")
    assert response.status_code == 200
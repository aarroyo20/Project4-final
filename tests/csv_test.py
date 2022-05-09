from flask import Flask, current_app
from app import db
import os
from app.db.models import Transaction
from app.transactions import transactions_upload
from tests.transactions_test import test_user
import logging
from app import config
from app.db.models import User


def test_access_transaction_denied(client):
    """Tests access to transactions dashboard"""
    response = client.get("/browse_transactions", follow_redirects=False)
    assert response.status_code == 404

def test_upload_csvfile__denied(client):
    """Tests user access for transactions dashboard"""
    response = client.get("/upload", follow_redirects=False)
    assert response.status_code == 404
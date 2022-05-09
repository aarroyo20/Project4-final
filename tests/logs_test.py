import logging
import os
import app.config


def test_logfile_handler():
    """Tests for handler log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/handler.log')
    assert os.path.exists(logfile) == True

def test_logfile_myapp():
    """Tests for myapp log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(logfile) == True

def test_logfile_request():
    """Tests for request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/request.log')
    assert os.path.exists(logfile) == True

def test_logfile_error():
    """Tests for errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/errors.log')
    assert os.path.exists(logfile) == True

def test_logfile_sqlalchemy():
    """Tests for sqlalchemy log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(logfile) == True

def test_logfile_werkzeug():
    """Tests for werkzeug log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(logfile) == True

def test_logfile_csvfile():
    """Tests for csvfile log"""
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/csvfile.log')
    assert os.path.exists(logfile) == True


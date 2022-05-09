import logging
import os
from pathlib import Path
from click.testing import CliRunner

from app import create_database
import logs
from app.db import config
runner = CliRunner()


def test_create_database():
    """Tests database directory available"""
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    # creates directory if it doesnt already exist
    assert os.path.exists(dbdir) == True

def test_create_uploads_folder():
    """Tests uploads folder available"""
    root = config.Config.BASE_DIR
    uploadfolder = os.path.join(root, '..', config.Config.UPLOAD_FOLDER)
    # creates directory if it doesnt already exist
    assert os.path.exists(uploadfolder) == True



# this test checks if the database directory is created#18
def test_auto_creat_database():
    """Tests database directory available"""
    root = config.Config.BASE_DIR
    dbdir = os.path.join(root,'..',config.Config.DB_DIR)
    # creates directory if it doesnt already exist
    assert os.path.exists(dbdir) == True

def test_create_log_folder():
    """Tests log folder availability"""
    logdir = config.Config.LOG_DIR
    path = Path(logdir)
    if path.is_file():
        print(f'The file {logs} exists')
    else:
        print(f'The file {logs} does not exist')
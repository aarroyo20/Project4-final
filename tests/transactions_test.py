import pytest
import os
from app import config
from app import db
from app.db.models import Transaction, User


@pytest.fixture
def test_user(application):
    """Tests adding and deleting user"""
    with application.app_context():
        assert db.session.query(User).count() == 0 # pylint: disable=no-member
        EMAIL = 'ara55@njit.edu'
        PASSWORD = 'Password'
        user = User(EMAIL,  PASSWORD )
        db.session.add(user) # pylint: disable=no-member
        db.session.commit() # pylint: disable=no-member
        yield user
        db.session.delete(user) # pylint: disable=no-member
        assert db.session.query(User).count() == 0 # pylint: disable=no-member
        assert db.session.query(Transaction).count() == 0 # pylint: disable=no-member


def test_transactions_db(application, test_user):
    """Tests db transactions """
    user = test_user
    assert db.session.query(Transaction).count() == 0
    transactions = []
    transactions.append( Transaction(50, 'Deposit') )
    transactions.append( Transaction(400, 'Withdrawal') )
    user.transactions += transactions
    db.session.commit()
    assert db.session.query(Transaction).count() == 2
    transactions1 = Transaction.query.filter_by(type='Deposit').first()
    assert transactions1.amount == 50
    transactions1.amount = 400
    db.session.commit()
    trans2 = Transaction.query.filter_by(amount=400).first()
    assert trans2.type == 'Deposit'
    db.session.delete(trans2)
    db.session.commit()
    assert db.session.query(Transaction).count() == 1


def test_transactions_upload_route(application, test_user):
    # pylint: disable=unused-argument,redefined-outer-name
    with application.test_client(test_user) as client:
        resp = client.get("/transactions/upload", follow_redirects=True)
        assert resp.status_code == 200


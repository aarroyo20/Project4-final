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
        PASSWORD = 'password'
        user = User(EMAIL,  PASSWORD )
        db.session.add(user) # pylint: disable=no-member
        db.session.commit() # pylint: disable=no-member
        yield user
        db.session.delete(user) # pylint: disable=no-member
        assert db.session.query(User).count() == 0 # pylint: disable=no-member
        assert db.session.query(Transaction).count() == 0 # pylint: disable=no-member



def test_transactions_db(application, test_user):
    """Tests transactions in database """
    user = test_user
    assert db.session.query(Transaction).count() == 0

    transactions = []
    transactions.append( Transaction(100, 'Deposit') )
    transactions.append( Transaction(20, 'Withdrawl') )
    user.transactions += transactions
    db.session.commit() # pylint: disable=no-member
    assert db.session.query(Transaction).count() == 2

    transactions1 = Transaction.query.filter_by(type='Deposit').first()
    assert transactions1.amount == 100
    transactions1.amount = 200
    db.session.commit() # pylint: disable=no-member
    trans2 = Transaction.query.filter_by(amount=200).first()
    assert trans2.type == 'Deposit'

    db.session.delete(trans2)
    db.session.commit()
    assert db.session.query(Transaction).count() == 1


def test_transactions_upload_route(application, test_user):
    # pylint: disable=unused-argument,redefined-outer-name
    with application.test_client(test_user) as client:
        resp = client.get("/transactions/upload", follow_redirects=True)
        assert resp.status_code == 200

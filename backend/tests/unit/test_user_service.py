import pytest
import sqlite3

from app.services.user_service import create_user, get_user
from app.models.user import CREATE_USERS_TABLE

db_path = "tests/clare_test.db"

@pytest.fixture
def test_conn():
    conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE)
    conn.commit()
    yield conn
    conn.close()


def test_create_user(test_conn):
  """Should create a user given expected user values"""
  user = {
    "name": "A",
    "email": "a@email.com",
    "password": "1234",
    "date_last_period": "2026-05-11",
    "rest_offset_before": 6,
    "rest_offset_after": 4,
  }
  res = create_user(user, test_conn)
  assert res == 1

def test_create_user_no_rest_offsets_provided(test_conn):
  """Should create a user even if rest_offset_before or rest_offset_after arent provided"""

  user = {
    "name": "B",
    "email": "b@email.com",
    "password": "5678",
    "date_last_period": "2026-06-12"
  }
  res = create_user(user, test_conn)
  assert res == 1

def test_create_user_no_required_field_provided(test_conn):
  """Should not create a user if a required field is not provided"""

  user = {
    "name": "C",
    "email": None,
    "password": "0000",
    "date_last_period": "2025-01-01"
  }

  res = create_user(user, test_conn)
  assert res == None

def test_create_user_email_exists(test_conn):
  """Should not create a user if a user with that email already exists"""

  user1 = {
    "name": "D",
    "email": "d@email.com",
    "password": "111a",
    "date_last_period": "2026-02-02"
  }
  user2 = {
      "name": "Dee",
      "email": "d@email.com",
      "password": "111b",
      "date_last_period": "2026-03-03"
    }



  res1 = create_user(user1, test_conn)
  res2 = create_user(user2, test_conn)
  assert res1 == 1
  assert res2 == None

def test_get_user(test_conn):
  """Should successfully retrieve a user from the db"""
  user = {
    "name": "A",
    "email": "a@email.com",
    "password": "1234",
    "date_last_period": "2026-05-11",
    "rest_offset_before": 6,
    "rest_offset_after": 4,
  }
  user_id = create_user(user, test_conn)

  res = get_user(user_id, test_conn)
  assert res == (1, "A", "a@email.com", "2026-05-11", 6, 4, None)


# TODO: Move the function below to a different place checking that the format is valid first, perhaps client side
# def test_create_user_invalid_date_format(test_conn):
#   """Should not create a user if the date provided is invalid"""

#   user = {
#     "name": "D",
#     "email": "d@email.com",
#     "password": "1111",
#     "date_last_period": "13-01-20206"
#   }

#   res = create_user(user, test_conn)
#   assert res == None



import sqlite3

from app.types.user import User
from app.models.user import CREATE_USER, GET_USER

def create_user(user:User, conn) -> int | None:
    try:
        new_user = (user["name"], user["email"], user["password"], user["date_last_period"], user.get("rest_offset_before", None), user.get("rest_offset_after", None))

        res = conn.execute(CREATE_USER, new_user)
        conn.commit()
        return res.lastrowid
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to create user:", e)
        return None

def get_user(userId: int, conn) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER)
        row = cur.fetchone()
        print(f"row: {row}")
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)



def get_user_for_auth(userID: int) -> User | None:
    pass
import sqlite3
from datetime import date

from app.types.user import User, UpdateUserPayload
from app.models.user import CREATE_USER, GET_USER, GET_USER_FOR_AUTH

def create_user(user:User, conn: sqlite3.Connection) -> int | None:
    try:
        new_user = (user["name"], user["email"], user["password"], date.fromisoformat(user["date_last_period"]), user.get("rest_offset_before", None), user.get("rest_offset_after", None))

        res = conn.execute(CREATE_USER, new_user)
        conn.commit()
        return res.lastrowid
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to create user:", e)
        return None

def get_user(userId: int, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER, (userId,))
        row = cur.fetchone()
        print(f"row: {row}")
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)

def get_user_for_auth(userId: int, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER_FOR_AUTH, (userId,))
        row = cur.fetchone()
        print(f"row: {row}")
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)

def update_user(userId: int, updateUserPayload: UpdateUserPayload, conn: sqlite3.Connection) -> User | None:
    try:
        # need to build query based on what the payload actually has set, making sure none of the values are None
        if updateUserPayload is None:
            return None
        query = "UPDATE users SET"
        for col in updateUserPayload:
            if col == "date_last_period":
                query += f"{col} = {date.fromisoformat(updateUserPayload[col])}"
            else:
                query += f"{col} = {updateUserPayload[col]},"
        query.removesuffix(",")
        query += "WHERE id = ?"

        conn.execute(query, (userId,))
        conn.commit()
        return get_user(userId, conn)
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to update user:", e)
        return None
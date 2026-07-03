import sqlite3
from datetime import date

from app.types.user import User, UpdateUserPayload
from app.models.user import CREATE_USER, GET_USER, GET_USER_FOR_AUTH

def create_user(user:User, conn: sqlite3.Connection) -> int | None:
    try:
        new_user = (user["name"], user["email"], user["password"], date.fromisoformat(user["date_last_period"]), user.get("rest_offset_before", 5), user.get("rest_offset_after", 5))

        res = conn.execute(CREATE_USER, new_user)
        conn.commit()
        return res.lastrowid
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to create user:", e)
        return None

def get_user(user_id: int, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER, (user_id,))
        row = cur.fetchone()
        print(f"row: {row}")
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)

def get_user_for_auth(user_id: int, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER_FOR_AUTH, (user_id,))
        row = cur.fetchone()
        print(f"row: {row}")
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)

def update_user(user_id: int, update_user_payload: UpdateUserPayload, conn: sqlite3.Connection) -> User | None:
    try:
        # need to build query based on what the payload actually has set, making sure none of the values are None
        if update_user_payload is None:
            return None
        query = "UPDATE users SET "
        for col in update_user_payload:
            if col == "date_last_period":
                query += f"{col} = '{date.fromisoformat(update_user_payload[col])}', "
            elif type(update_user_payload[col]) == str:
              query += f"{col} = '{update_user_payload[col]}', "
            else:
                query += f"{col} = {update_user_payload[col]}, "
        query = query.removesuffix(", ")
        print("query:", query)
        query += " WHERE id = ?"
        print("full query:", query)

        conn.execute(query, (user_id,))
        conn.commit()
        return get_user(user_id, conn)
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to update user:", e)
        return None
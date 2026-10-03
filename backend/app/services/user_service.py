import sqlite3
from datetime import date

from app.types.user import (
    User,
    SignUpPayload,
    UpdateUserPayload,
    UpdateUserPasswordPayload,
)
from app.models.user import CREATE_USER, GET_USER, GET_USER_FOR_AUTH, DELETE_USER


def create_user(user: SignUpPayload, conn: sqlite3.Connection) -> int | None:
    try:
        new_user = (user["name"], user["email"], user["password"])

        res = conn.execute(CREATE_USER, new_user)
        conn.commit()
        return res.lastrowid
    except sqlite3.Error as e:
        print("Failed to create user:", e)
        return None


def get_user(user_id: int, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER, (user_id,))
        row: User | None = cur.fetchone()
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)
        return None


def get_user_for_auth(email: str, conn: sqlite3.Connection) -> User | None:
    try:
        cur = conn.cursor()
        cur.execute(GET_USER_FOR_AUTH, (email,))
        row: User | None = cur.fetchone()
        return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)
        return None


def update_user(
    user_id: int, update_user_payload: UpdateUserPayload, conn: sqlite3.Connection
) -> User | None:
    try:
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
        query += " WHERE id = ?"
        conn.execute(query, (user_id,))
        conn.commit()
        return get_user(user_id, conn)
    except ValueError as e:
        print("Invalid date format given: use YYYY-MM-DD")
    except sqlite3.Error as e:
        print("Failed to update user:", e)
        return None


def delete_user(user_id: int, conn: sqlite3.Connection) -> bool | None:
    try:
        user = get_user(user_id, conn)
        if user is None:
            return False
        conn.execute(DELETE_USER, (user_id,))
        return True

    except sqlite3.Error as e:
        print("Failed to delete user:", e)
        return None


# TODO: Finish working on update_user_password after auth is sorted
# def update_user_password(user_id: int, update_user_password_payload: UpdateUserPasswordPayload, conn: sqlite3.Connection):
#     try:

#     except sqlite3.Error as e:
#         print("Failed to update user:", e)
#         return None

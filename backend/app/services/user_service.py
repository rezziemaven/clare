import sqlite3

from types.user import User

def create_user(user:User) -> int | None:
    # open connection
    query = """INSERT INTO users
    (name, email, password, date_last_period, rest_offset_before, rest_offset_after)
    VALUES(?,?,?,?,?,?)"""

    try:
        new_user = (user["name"], user["email"], user["password"], user["date_last_period"], user.get("rest_offset_before", None), user.get("rest_offset_after", None))

        with sqlite3.connect("app/models/clare.db") as conn:
            cur = conn.cursor()
            cur.execute(query, new_user)
            conn.commit()
            return cur.lastrowid
    except sqlite3.Error as e:
        print("Failed to create user:", e)
        return None

def get_user(userId: int) -> User | None:
    query = """SELECT email, date_last_period, rest_offset_before, rest_offset_after, calendar_url FROM users"""

    try:
        with sqlite3.connect("app/models/clare.db") as conn:
            cur = conn.cursor()
            cur.execute(query)
            row = cur.fetchone()
            return row
    except sqlite3.Error as e:
        print("Failed to get user:", e)



def get_user_for_auth(userID: int) -> User | None:
    pass
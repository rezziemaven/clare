import sqlite3

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        date_last_period DATE NOT NULL,
        rest_offset_before INTEGER DEFAULT "5",
        rest_offset_after INTEGER DEFAULT "5",
        calendar_url TEXT
        );"""

CREATE_USER = """INSERT INTO users
(name, email, password, date_last_period, rest_offset_before, rest_offset_after)
VALUES(?,?,?,?,?,?)"""

GET_USER = """SELECT id, name, email, date_last_period, rest_offset_before, rest_offset_after, calendar_url FROM users"""

    try:
        with sqlite3.connect("app/models/clare.db") as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            print("User table created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create user table:", e)



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

    try:
        with sqlite3.connect("app/models/clare.db") as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            print("User table created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create user table:", e)



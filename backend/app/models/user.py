import sqlite3

def user_model() -> sqlite3.Cursor | None:
    query = """CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        date_last_period DATE NOT NULL,
        rest_offset_before INTEGER DEFAULT "5" NOT NULL,
        rest_offset_after INTEGER DEFAULT "5" NOT NULL,
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



from app.utils.sqlite import sqlite3

def get_conn():
    try:
        conn = sqlite3.connect("app/models/clare.db", detect_types=sqlite3.PARSE_DECLTYPES)
        return conn
    except sqlite3.Error as e:
        print("Failed to create connection:", e)
        return None
import sqlite3

def get_conn():
    try:
        conn = sqlite3.connect("app/models/clare.db")
        return conn
    except sqlite3.Error as e:
        print("Failed to create connection:", e)
        return None
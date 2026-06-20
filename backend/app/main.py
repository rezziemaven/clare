import sqlite3
from models.user import user_model

def main():
    user_model()
    print("Database created.")

if __name__ == "__main__":
    main()

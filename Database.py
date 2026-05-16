import sqlite3

DB_NAME = "flowers.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS flowers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            last_watered TEXT NOT NULL,
            last_fertilized TEXT,
            fertilize BOOLEAN NOT NULL
        )
    """)

    conn.commit()
    conn.close()
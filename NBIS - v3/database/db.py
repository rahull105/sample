import sqlite3

def get_db():
    conn = sqlite3.connect("nbis.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            latitude REAL,
            longitude REAL
        )
    """)

    conn.commit()
    conn.close()

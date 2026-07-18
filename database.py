import sqlite3

DB_NAME = "clanhq.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS war_signups (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_signup(user_id, username, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO war_signups
        (user_id, username, status)
        VALUES (?, ?, ?)
    """, (user_id, username, status))

    conn.commit()
    conn.close()


def get_signups():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, status
        FROM war_signups
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def clear_signups():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM war_signups")

    conn.commit()
    conn.close()

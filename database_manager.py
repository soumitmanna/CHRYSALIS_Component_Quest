import sqlite3

DATABASE_NAME = "inventory.db"


def create_database():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        component TEXT NOT NULL,
        confidence REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_component(component, confidence):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO inventory
        (component, confidence)
        VALUES (?, ?)
        """,
        (component, confidence)
    )

    conn.commit()
    conn.close()


def get_all_components():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM inventory
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
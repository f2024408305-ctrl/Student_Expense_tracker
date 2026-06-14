# Database Module

import sqlite3

def connect_db():
    conn = sqlite3.connect("database/expenses.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

print("Database module loaded")

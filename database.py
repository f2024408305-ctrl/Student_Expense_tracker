import sqlite3

def get_connection():
    """Establishes a connection to the SQLite database file."""
    return sqlite3.connect("expenses.db")


def initialize_db():
    """Creates the expenses table structure if it doesn't exist yet."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")


def add_expense(title, amount, category, date_str):
    """Inserts a new row of data into the expenses table."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Using '?' placeholders protects your application from SQL injection attacks
    cursor.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, amount, category, date_str))
    
    conn.commit()
    conn.close()
    print(f"Successfully saved to database: {title}")


# This block ensures the code below ONLY runs if you run database.py directly.
# When dashboard.py or add_expense.py imports this file, this test code is ignored.
if __name__ == "__main__":
    print("--- Running Database Test ---")
    initialize_db()
    add_expense("Test Coffee", 4.50, "Food", "2026-06-18")
    print("--- Test Finished Without Errors! ---")
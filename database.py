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
    
    cursor.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, amount, category, date_str))
    
    conn.commit()
    conn.close()
    print(f"Successfully saved to database: {title}")


def fetch_all_expenses():
    """Fetches all rows from the expenses table, ordered by newest date first."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title, amount, category, date FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    
    conn.close()
    return rows  # Sends the data back to the Treeview table!


if __name__ == "__main__":
    print("--- Running Database Test ---")
    initialize_db()
    add_expense("Test Coffee", 4.50, "Food", "2026-06-18")
    print("--- Test Finished Without Errors! ---")
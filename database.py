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




def fetch_expense_summary():
    """Calculates total spending and aggregates totals grouped by category."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Get overall total spending
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_result = cursor.fetchone()[0]
    total_spent = total_result if total_result is not None else 0.0
    
    # 2. Get total breakdown per category, ordered by highest spent first
    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses 
        GROUP BY category 
        ORDER BY SUM(amount) DESC
    """)
    category_breakdown = cursor.fetchall()
    
    conn.close()
    return total_spent, category_breakdown

def delete_expense(expense_id):
    """Deletes a specific expense record based on its unique ID."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Use parameterized query '?' to prevent accidental deletions or SQL injection
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    
    conn.commit()
    conn.close()
    print(f"Record with ID {expense_id} deleted successfully.")
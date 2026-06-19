import tkinter as tk
from tkinter import ttk
import database

print("Functions inside database module:", dir(database))
print("Inside the correct view_expense file!")

def open_view_expenses_window(parent_window):
    """Creates a popup window to fetch and display saved expenses in a table format."""
    view_win = tk.Toplevel(parent_window)
    view_win.title("View Expenses")
    view_win.geometry("600x480")  # 👈 Expanded height slightly to fit the delete button cleanly
    view_win.grab_set()

    tk.Label(view_win, text="Saved Expenses Log", font=("Arial", 14, "bold")).pack(pady=10)

    columns = ("id", "title", "amount", "category", "date")
    table = ttk.Treeview(view_win, columns=columns, show="headings", height=12)
    
    table.heading("id", text="ID")
    table.heading("title", text="Title")
    table.heading("amount", text="Amount ($)")
    table.heading("category", text="Category")
    table.heading("date", text="Date")

    table.column("id", width=50, anchor="center")
    table.column("title", width=150, anchor="w")
    table.column("amount", width=100, anchor="e")
    table.column("category", width=120, anchor="center")
    table.column("date", width=120, anchor="center")
    
    table.pack(pady=10, padx=10, fill="both", expand=True)

    # ========================================================
    # 🛠️ HELPER FUNCTION (Moved inside so it can access 'table')
    # ========================================================
    def delete_selected():
        # 1. Find out which row the user highlighted in the spreadsheet grid
        selected_item = table.selection()  # 👈 Fixed: Changed 'tree' to 'table'
        
        if not selected_item:
            print("Please select an expense from the list to delete.")
            return
            
        # 2. Extract the values of that row
        item_data = table.item(selected_item)  # 👈 Fixed: Changed 'tree' to 'table'
        record_values = item_data['values']
        
        # 3. Grab the unique database 'id'
        record_id = record_values[0]
        
        # 4. Fire the deletion query in database.py
        database.delete_expense(record_id)
        
        # 5. Instantly remove the row visually from your screen grid
        table.delete(selected_item)  # 👈 Fixed: Changed 'tree' to 'table'

    # ========================================================
    # 🎨 UI BUTTON WIDGET (Placed cleanly underneath the table)
    # ========================================================
    btn_delete = tk.Button(
        view_win, 
        text="❌ Delete Selected", 
        width=20, 
        bg="#e74c3c", 
        fg="white", 
        font=("Arial", 10, "bold"),
        command=delete_selected
    )
    btn_delete.pack(pady=15)

    # Populates the table with database rows
    try:
        expenses = database.fetch_all_expenses()
        for row in expenses:
            table.insert("", "end", values=row)
    except AttributeError:
        table.insert("", "end", values=("ERROR", "Please update database.py", "", "", ""))
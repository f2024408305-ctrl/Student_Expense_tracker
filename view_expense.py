import tkinter as tk
from tkinter import ttk
import database

print("Functions inside database module:", dir(database))

print("Inside the correct view_expense file!")

def open_view_expenses_window(parent_window):
    """Creates a popup window to fetch and display saved expenses in a table format."""
    view_win = tk.Toplevel(parent_window)
    view_win.title("View Expenses")
    view_win.geometry("600x400")
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

    try:
        expenses = database.fetch_all_expenses()
        for row in expenses:
            table.insert("", "end", values=row)
    except AttributeError:
        table.insert("", "end", values=("ERROR", "Please update database.py", "", "", ""))
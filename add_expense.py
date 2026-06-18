import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
import database  # Connects directly to your database script!

def open_add_expense_window(parent_window):
    """Creates a popup window to input and save an expense."""
    
    # 1. Create a child popup window linked to the dashboard
    add_win = tk.Toplevel(parent_window)
    add_win.title("Add New Expense")
    add_win.geometry("320x400")
    
    # Freeze interaction with the main dashboard until this window closes
    add_win.grab_set()

    # 2. Form Layout (Labels & Entry Fields)
    tk.Label(add_win, text="Expense Title:", font=("Arial", 10, "bold")).pack(pady=5)
    title_entry = tk.Entry(add_win, width=30)
    title_entry.pack(pady=5)

    tk.Label(add_win, text="Amount ($):", font=("Arial", 10, "bold")).pack(pady=5)
    amount_entry = tk.Entry(add_win, width=30)
    amount_entry.pack(pady=5)

    tk.Label(add_win, text="Category:", font=("Arial", 10, "bold")).pack(pady=5)
    category_dropdown = ttk.Combobox(add_win, values=["Food", "Rent", "Utilities", "Entertainment", "Other"], width=27)
    category_dropdown.pack(pady=5)

    # 3. Form Processing Logic
    def handle_save():
        title = title_entry.get().strip()
        amount_raw = amount_entry.get().strip()
        category = category_dropdown.get()

        # Input Validation: Prevent empty fields
        if not title or not amount_raw or not category:
            messagebox.showwarning("Validation Error", "All fields are required!", parent=add_win)
            return

        # Input Validation: Ensure amount is numeric
        try:
            amount = float(amount_raw)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid number!", parent=add_win)
            return

        # Automatically capture today's date (2026)
        from datetime import date
        today = date.today().strftime("%Y-%m-%d")

        # Send data straight to your database layer! 🚀
        database.add_expense(title, amount, category, today)
        
        # Confirmation popup & close window cleanly
        messagebox.showinfo("Success", "Expense added successfully!", parent=add_win)
        add_win.destroy()

    # 4. Save Button
    save_btn = tk.Button(add_win, text="Save Expense", command=handle_save, bg="#2ecc71", fg="white", width=15, font=("Arial", 10, "bold"))
    save_btn.pack(pady=25)

    